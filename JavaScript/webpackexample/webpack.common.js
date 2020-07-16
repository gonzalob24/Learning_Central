const path = require("path");
var HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
    // remove mode in common webpack file
    // remove output file because in dev version I dont want contentHash in production version I do
    entry: "./src/index.js",
    plugins: [new HtmlWebpackPlugin({
        template: "./src/template.html"
    })],
    module: {
        rules: [
            {
                test: /\.scss$/, // webpack needs to know about this so I imported main.css in index.js. I can just use .scss becuase scss is not valid css code. So, I have to use another loader. Use sass-loader --> turns code into valid css and then css and style loader will take care of the rest.
                use: [
                    "style-loader", //3. Inject styles into DOM
                    "css-loader", // 2. Turns css into JS code
                    "sass-loader" // 1. Turns sass into valid css
                ] // takes sass turn into valid css code, css-loader turns file into valid JS code and style injects code into the DOM
            },
            {
                test: /\.html$/i,
                use: ["html-loader"] // Iam requiring every image but then webpacl does not know what to do with
                                    // it so I need to use file-loader to handle the required images.
            },
            {
                test: /\.(svg|png|jpg|gif)$/,
                use: {
                    loader: "file-loader",
                    options: { // I can provide some options and make a copy of the file and move it to dist
                        name: "[name].[hash].[ext]",
                        outputPath: "imgs"
                    }    
                }        
            }
        ]
    },

}