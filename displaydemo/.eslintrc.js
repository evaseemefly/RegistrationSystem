module.exports = {
  // 默认情况下，ESLint会在所有父级组件中寻找配置文件，一直到根目录。ESLint一旦发现配置文件中有 "root": true，它就会停止在父级目录中寻找。
  root: true,
  // 对Babel解析器的包装使其与 ESLint 兼容。
  parser: 'babel-eslint',
  env: {
    es6: true,
    node: true,
    browser: true,
    commonjs: true,
    jquery: true
  },
  // 扩展一个流行的风格指南，即 eslint-config-standard 
  // https://github.com/feross/standard/blob/master/RULES.md#javascript-standard-style
  extends: 'standard',
  // required to lint *.vue files
  plugins: [
    // 此插件用来识别.html 和 .vue文件中的js代码
    'html',
    // standard风格的依赖包
    "standard",
    // standard风格的依赖包
    "promise"
  ],
  parserOptions: {
    ecmaVersion: 2015,
    sourceType: "module"
  },
  rules: {
    indent: ["error", "tab"],
    "linebreak-style": ["error", "windows"],
    quotes: ["error", "double"],
    semi: ["error", "always"]
  }
};
