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

int main() {
    int sockfd;
    struct sockaddr_in servaddr;
    char buffer[BUFFER_SIZE];

    // Create UDP socket
    if ((sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&servaddr, 0, sizeof(servaddr));

    // Filling server information
    servaddr.sin_family = AF_INET; // IPv4
    servaddr.sin_addr.s_addr = inet_addr("20.244.51.20"); // IP address of the target (localhost in this case)
    servaddr.sin_port = htons(PORT);

    while (1) {
        // Create a MAVLink heartbeat message
        mavlink_message_t msg;
        uint8_t buf[MAVLINK_MAX_PACKET_LEN];
        mavlink_heartbeat_t heartbeat;
        heartbeat.type = MAV_TYPE_GCS;
        heartbeat.autopilot = MAV_AUTOPILOT_INVALID;
        heartbeat.base_mode = 0;
        heartbeat.custom_mode = 0;
        heartbeat.system_status = MAV_STATE_ACTIVE;
        mavlink_msg_heartbeat_encode(0, MAV_COMP_ID_SYSTEM_CONTROL, &msg, &heartbeat);

        // Print the individual fields of the heartbeat message
        printf("Sending MAVLink heartbeat message:\n");
        printf("Type: %d\n", heartbeat.type);
        printf("Autopilot: %d\n", heartbeat.autopilot);
        printf("Base Mode: %d\n", heartbeat.base_mode);
        printf("Custom Mode: %d\n", heartbeat.custom_mode);
        printf("System Status: %d\n", heartbeat.system_status);

        // Serialize the message
        uint16_t len = mavlink_msg_to_send_buffer(buf, &msg);

        // Send the message
        if (sendto(sockfd, buf, len, 0, (const struct sockaddr *)&servaddr, sizeof(servaddr)) < 0) {
            perror("sendto failed");
            exit(EXIT_FAILURE);
        }

        sleep(1); // Delay for 1 second before sending the next message
    }

    close(sockfd);
    return 0;
}
