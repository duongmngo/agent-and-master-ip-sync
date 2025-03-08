module.exports = {
  apps: [
    {
      name: "IP Sync Master",
      script: "master.py",
      interpreter: "python",
      env: {
        SECRET_TOKEN: "",
      },
    },
  ],
};
