module.exports = {
  apps: [
    {
      name: "IP Sync Agent",
      script: "agent.py",
      interpreter: "python",
      env: {
        MASTER_URL: "",
        SECRET_TOKEN: "",
      },
    },
  ],
};
