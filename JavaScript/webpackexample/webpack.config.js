const path = require("path");

module.exports = {
    mode: "development",
    entry: "./src/index.js",
    output: {
        filename: "main.js",
        path: path.resolve(__dirname, "dist")
    },
    module: {
        rules: [
            {
                test: /\.css$/, // webpack needs to know about this so I imported main.css in index.js
                use: ["style-loader", "css-loader"], // takes css file and turns it into valid JS code
            }
        ]
    },

}