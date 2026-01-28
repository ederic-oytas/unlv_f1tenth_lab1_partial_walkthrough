import rclpy
from rclpy.node import Node

from ackermann_msgs.msg import AckermannDriveStamped


class TalkerNode(Node):
    def __init__(self) -> None:
        super().__init__("talker_node")

        self.declare_parameter("my_parameter")
        value = self.get_parameter("my_parameter").value

        self.create_timer(2.0, self.timer_callback)

        self.my_topic_pub = self.create_publisher(
            AckermannDriveStamped, "/my_topic", 10
        )

        self.get_logger().info(f"talker_node initialized with {value}")

    def timer_callback(self) -> None:
        self.get_logger().info("Timer callback called.")

        msg = AckermannDriveStamped()
        msg.drive.speed = 2.5

        self.my_topic_pub.publish(msg)


def main() -> None:
    rclpy.init()
    node = TalkerNode()
    rclpy.spin(node)
    rclpy.shutdown()
