
# Lab 1 Partial Walkthrough

These are the files for the lab 1 partial walkthrough that I used on Thursday, January 22nd.

Some notes:

* `lab1_pkg/lab1_pkg/talker.py` - Uses publishers and parameters.
* `lab1_pkg/lab1_pkg/listener.py` - Uses subscriptions.
* `lab1_pkg/setup.py` - Makes entrypoints available and also **installs the launch file as a data file**,
  so you can use `ros2 launch <package_name> <launch_file>` instead of using `ros2 launch <path_to_launch_file>`
* `lab1_pkg/launch/lab1_launch.py` - Declares launch arguments and passes them to talker, launches talker and listener nodes.
