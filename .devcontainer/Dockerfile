FROM osrf/ros:humble-desktop-full

ARG WORKSPACE=dev_container
WORKDIR /workspace/$WORKSPACE

ENV TERM xterm
ENV SHELL /bin/zsh

RUN apt-get update && apt-get install -y \
    wget \
    ros-humble-robot-localization \
    ros-humble-ros2bag \
    ros-humble-rosbag2-storage-default-plugins

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" -- \
    -p git \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-completions

RUN echo "export DISABLE_AUTO_TITLE=true" >> /root/.zshrc
RUN echo 'LC_NUMERIC="en_US.UTF-8"' >> /root/.zshrc
RUN echo "source /opt/ros/humble/setup.zsh" >> /root/.zshrc

# Restore autocomplete for the ros2 & colcon tools.
RUN echo "autoload -U bashcompinit" >> /root/.zshrc
RUN echo "bashcompinit" >> /root/.zshrc
RUN echo 'eval "$(register-python-argcomplete3 ros2)"' >> /root/.zshrc
RUN echo 'eval "$(register-python-argcomplete3 colcon)"' >> /root/.zshrc

CMD ["zsh"]