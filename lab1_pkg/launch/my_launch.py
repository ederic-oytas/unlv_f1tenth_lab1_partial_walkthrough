from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    args = []

    my_argument_arg = DeclareLaunchArgument("my_argument")
    args.append(my_argument_arg)

    nodes = []

    talker_node = Node(
        package="lab1_pkg",
        executable="talker",
        name="talker_node",
        parameters=[{"my_parameter": LaunchConfiguration("my_argument")}],
    )
    nodes.append(talker_node)
    listener_node = Node(
        package="lab1_pkg",
        executable="listener",
        name="listener_node",
    )
    nodes.append(listener_node)

    return LaunchDescription(args + nodes)
