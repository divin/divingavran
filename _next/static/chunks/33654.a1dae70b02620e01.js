(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[33654,93279],{33654:function(e,t,a){"use strict";var n=a(64836);Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var r=n(a(2329)).default;t.default=r},2329:function(e){"use strict";function t4Templating(e){!function(e){function createBlock(e,t,a){return{pattern:RegExp("<#"+e+"[\\s\\S]*?#>"),alias:"block",inside:{delimiter:{pattern:RegExp("^<#"+e+"|#>$"),alias:"important"},content:{pattern:/[\s\S]+/,inside:t,alias:a}}}}function createT4(t){var a=e.languages[t],n="language-"+t;return{block:{pattern:/<#[\s\S]+?#>/,inside:{directive:createBlock("@",{"attr-value":{pattern:/=(?:("|')(?:\\[\s\S]|(?!\1)[^\\])*\1|[^\s'">=]+)/,inside:{punctuation:/^=|^["']|["']$/}},keyword:/\b\w+(?=\s)/,"attr-name":/\b\w+/}),expression:createBlock("=",a,n),"class-feature":createBlock("\\+",a,n),standard:createBlock("",a,n)}}}}e.languages["t4-templating"]=Object.defineProperty({},"createT4",{value:createT4})}(e)}e.exports=t4Templating,t4Templating.displayName="t4Templating",t4Templating.aliases=[]},64836:function(e){function _interopRequireDefault(e){return e&&e.__esModule?e:{default:e}}e.exports=_interopRequireDefault,e.exports.__esModule=!0,e.exports.default=e.exports}}]);