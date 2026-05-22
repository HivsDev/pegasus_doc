// 海思文档社区自定义脚本
document.addEventListener('DOMContentLoaded', function() {
  // 添加页面加载动画
  var content = document.querySelector('.md-content');
  if (content) {
    content.style.opacity = '0';
    content.style.transition = 'opacity 0.3s ease';
    setTimeout(function() {
      content.style.opacity = '1';
    }, 100);
  }

  // 在代码块右上角显示语言标签
  var codeBlocks = document.querySelectorAll('div.highlight pre');
  codeBlocks.forEach(function(block) {
    var parent = block.closest('div.highlight');
    if (parent && !parent.querySelector('.lang-label')) {
      var label = document.createElement('span');
      label.className = 'lang-label';
      label.style.cssText = 'position:absolute;top:5px;right:10px;font-size:11px;color:#999;';
      parent.style.position = 'relative';
      parent.appendChild(label);
    }
  });
});
