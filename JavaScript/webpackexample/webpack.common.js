const path = require("path");

module.exports = {
  // remove mode in common webpack file
  // remove output file because in dev version I dont want contentHash in production version I do
  entry: {
    main: "./src/index.js",
    vendor: "./src/vendor.js",
  },
  module: {
    rules: [
      {
        test: /\.html$/i,
        use: ["html-loader"], // Iam requiring every image but then webpacl does not know what to do with
        // it so I need to use file-loader to handle the required images.
      },
      {
        test: /\.(svg|png|jpg|gif)$/,
        use: {
          loader: "file-loader",
          options: {
            // I can provide some options and make a copy of the file and move it to dist
            name: "[name].[hash].[ext]",
            outputPath: "imgs",
          },
        },
      },
    ],
  },
};
