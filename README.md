# mcploaddata

# Text Length Predictor

这是一个基于 FastAPI 实现的简单文本处理 MCP 服务，输入文本返回其长度。

## 📦 安装依赖

```bash
pip install fastapi uvicorn pydantic
🚀 启动服务

uvicorn app:app --host 0.0.0.0 --port 80
📡 接口说明
POST /predict

请求示例：

{
  "text": "Hello, world!"
}
响应示例：


{
  "length": 13,
  "input": "Hello, world!"
}
⚙️ MCP 服务配置

{
  "name": "text-length-predictor",
  "type": "http",
  "command": "uvx",
  "args": ["app:app", "--host", "0.0.0.0", "--port", "80"],
  "port": 80,
  "protocol": "HTTP",
  "entry": "app:app",
  "healthcheck": "/predict",
  "env": {}
}
