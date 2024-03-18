#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <string.h>

#include "mavlink/generated/include/mavlink/v2.0/common/mavlink.h"

#define PORT 14550
#define BUFFER_SIZE 1024

// Function to interpret and print the received MAVLink message
void interpret_mavlink_message(const mavlink_message_t *msg) {
    switch (msg->msgid) {
        case MAVLINK_MSG_ID_HEARTBEAT: {
            mavlink_heartbeat_t heartbeat;
            mavlink_msg_heartbeat_decode(msg, &heartbeat);
            printf("Received heartbeat message\n");
            printf("Type: %d\n", heartbeat.type);
            printf("Autopilot: %d\n", heartbeat.autopilot);
            // Print other fields as needed
            break;
        }
        // Add cases for other message IDs as needed
        default:
            printf("Received message with ID=%d, Length=%d\n", msg->msgid, msg->len);
            printf("Payload: ");
            for (int i = 0; i < msg->len; ++i) {
                printf("%02X ", ((unsigned char *)(&msg->payload64))[i]);
            }
            printf("\n");
            break;
    }
}

int main() {
    int sockfd;
    struct sockaddr_in servaddr, cliaddr;
    socklen_t len = sizeof(cliaddr);
    char buffer[BUFFER_SIZE];

    // Create UDP socket
    if ((sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&servaddr, 0, sizeof(servaddr));
    memset(&cliaddr, 0, sizeof(cliaddr));

    // Filling server information
    servaddr.sin_family = AF_INET; // IPv4
    servaddr.sin_addr.s_addr = INADDR_ANY;
    servaddr.sin_port = htons(PORT);

    // Bind the socket with the server address
    if (bind(sockfd, (const struct sockaddr *)&servaddr, sizeof(servaddr)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    printf("UDP server is listening...\n");

    // Continuously receive messages
    while (1) {
        int n = recvfrom(sockfd, (char *)buffer, BUFFER_SIZE, MSG_WAITALL, (struct sockaddr *)&cliaddr, &len);
        buffer[n] = '\0';

        // Parse the MAVLink message
        mavlink_message_t msg;
        mavlink_status_t status;
        for (int i = 0; i < n; ++i) {
            if (mavlink_parse_char(MAVLINK_COMM_0, buffer[i], &msg, &status)) {
                // Message parsed successfully
                interpret_mavlink_message(&msg);
            }
        }
    }

    close(sockfd);
    return 0;
}
