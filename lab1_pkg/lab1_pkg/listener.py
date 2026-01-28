import rclpy
from rclpy.node import Node

from ackermann_msgs.msg import AckermannDriveStamped

from tf2_ros import Buffer


class ListenerNode(Node):
    def __init__(self) -> None:
        super().__init__("listener_node")

        self.create_subscription(
            AckermannDriveStamped,
            "/my_topic",
            self.my_topic_callback,
            10,
        )

        self.get_logger().info("listener_node initialized")

    def my_topic_callback(self, drive_msg: AckermannDriveStamped) -> None:
        speed = drive_msg.drive.speed
        self.get_logger().info(f"my_topic_callback called with speed={speed}")


def main() -> None:
    rclpy.init()
    node = ListenerNode()
    rclpy.spin(node)
    rclpy.shutdown()
