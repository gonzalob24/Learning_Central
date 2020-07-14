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
                test: /\.scss$/, // webpack needs to know about this so I imported main.css in index.js. I can just use .scss becuase scss is not valid css code. So, I have to use another loader. Use sass-loader --> turns code into valid css and then css and style loader will take care of the rest.
                use: [
                    "style-loader", //3. Inject styles into DOM
                    "css-loader", // 2. Turns css into JS code
                    "sass-loader" // 1. Turns sass into valid css
                ], // takes sass turn into valid css code, css-loader turns file into valid JS code and style injects code into the DOM
            }
        ]
    },

}