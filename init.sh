echo "install ngrok..."
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null
echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list >/dev/null
sudo apt update >/dev/null
sudo apt install ngrok >/dev/null
echo "install code-server..."
curl -fsSL https://code-server.dev/install.sh | sh >/dev/null