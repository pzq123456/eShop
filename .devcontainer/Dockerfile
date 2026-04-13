# 明确使用你指定的镜像
FROM nvidia/cuda:13.2.0-cudnn-devel-ubuntu24.04

# 避免交互式安装时的时区确认提示
ENV DEBIAN_FRONTEND=noninteractive

# 安装 Python 3.12 及必要工具
RUN apt-get update && apt-get install -y \
    python3.12 \
    python3-pip \
    python3.12-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# 将 python 指向 python3.12
RUN ln -s /usr/bin/python3.12 /usr/bin/python

# 安装支持 Blackwell 架构 (RTX 50 系列) 的 PyTorch
# 注意：必须使用 nightly 或支持 sm_120 的版本
RUN pip install --no-cache-dir --break-system-packages \
    --pre torch torchvision torchaudio \
    --index-url https://download.pytorch.org/whl/nightly/cu128