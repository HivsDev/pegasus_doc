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

  // ========== 首页布局：隐藏右侧目录栏 ==========

  function setupHomepageLayout() {
    var path = window.location.pathname.replace(/\/+$/, '');
    var isHomepage = path === '/pegasus_doc'
      || path === '/pegasus_doc/index.html'
      || path === '/pegasus_doc/cn'
      || path === '/pegasus_doc/cn/index.html'
      || path === '/pegasus_doc/en'
      || path === '/pegasus_doc/en/index.html'
      || path === '/cn'
      || path === '/cn/index.html'
      || path === '/en'
      || path === '/en/index.html'
      || path === ''
      || path === '/'
      || path === '/index.html';

    if (isHomepage) {
      document.body.classList.add('homepage');
      var rightSidebar = document.querySelector('.md-sidebar--secondary');
      if (rightSidebar) {
        rightSidebar.style.display = 'none';
        rightSidebar.setAttribute('hidden', '');
      }
    }
  }

  setupHomepageLayout();

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

  // ========== 意见反馈系统 ==========

  var GITHUB_REPO = 'HivsDev/pegasus_doc';

  // 创建反馈按钮
  var fab = document.createElement('a');
  fab.className = 'feedback-fab';
  fab.href = '#';
  fab.setAttribute('role', 'button');
  fab.innerHTML = '<span class="fab-icon">&#9993;</span><span class="fab-label">意见反馈</span>';
  document.body.appendChild(fab);

  // 创建遮罩层
  var overlay = document.createElement('div');
  overlay.className = 'feedback-overlay';
  overlay.innerHTML = `
    <div class="feedback-modal">
      <div class="feedback-modal-header">
        <h3><span>&#9993;</span> 意见反馈</h3>
        <button class="feedback-modal-close">&times;</button>
      </div>
      <div class="feedback-modal-body">
        <!-- 表单区域 -->
        <div id="feedback-form-area">
          <div class="feedback-field">
            <label for="fb-page">当前页面</label>
            <input type="text" id="fb-page" readonly>
          </div>
          <div class="feedback-field">
            <label for="fb-type">反馈类型 <span class="required">*</span></label>
            <select id="fb-type">
              <option value="">请选择</option>
              <option value="文档错误">文档错误（描述不清、错别字、格式问题）</option>
              <option value="内容缺失">内容缺失（缺少必要说明、接口、示例）</option>
              <option value="示例问题">示例代码问题（编译失败、运行异常）</option>
              <option value="改进建议">改进建议（排版优化、内容补充建议）</option>
              <option value="其他">其他</option>
            </select>
          </div>
          <div class="feedback-field">
            <label for="fb-desc">问题描述 <span class="required">*</span></label>
            <textarea id="fb-desc" placeholder="请详细描述您遇到的问题或改进建议..."></textarea>
          </div>
          <div class="feedback-field">
            <label for="fb-name">您的称呼</label>
            <input type="text" id="fb-name" placeholder="可选">
          </div>
          <div class="feedback-field">
            <label for="fb-contact">联系方式（邮箱 / 微信 / 手机）</label>
            <input type="text" id="fb-contact" placeholder="可选，方便我们与您联系">
          </div>
          <button class="feedback-submit" id="fb-submit">
            <span>&#10148;</span> 提交反馈（将跳转到 GitHub Issue）
          </button>
          <div class="feedback-field" style="margin-bottom:0">
            <div class="field-hint">提交后将跳转到 GitHub Issues 页面，点击 "Submit new issue" 即可完成提交。需要 GitHub 账号。</div>
          </div>
        </div>
        <!-- 成功区域 -->
        <div class="feedback-success" id="feedback-success-area">
          <div class="success-icon">&#10004;</div>
          <h4>感谢您的反馈！</h4>
          <p>您的意见已提交到 GitHub Issues。</p>
          <p>请在新页面确认并点击 "Submit new issue" 完成提交。</p>
          <div class="success-note">我们会在收到后尽快处理。</div>
        </div>
      </div>
    </div>
  `;
  document.body.appendChild(overlay);

  // DOM 元素引用
  var modal = overlay.querySelector('.feedback-modal');
  var closeBtn = overlay.querySelector('.feedback-modal-close');
  var pageField = document.getElementById('fb-page');
  var typeField = document.getElementById('fb-type');
  var descField = document.getElementById('fb-desc');
  var nameField = document.getElementById('fb-name');
  var contactField = document.getElementById('fb-contact');
  var submitBtn = document.getElementById('fb-submit');
  var formArea = document.getElementById('feedback-form-area');
  var successArea = document.getElementById('feedback-success-area');

  // 页面 URL
  pageField.value = window.location.href;

  // 打开模态框
  fab.addEventListener('click', function(e) {
    e.preventDefault();
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
    // 重置表单
    formArea.style.display = 'block';
    successArea.classList.remove('active');
    descField.value = '';
    typeField.value = '';
    nameField.value = '';
    contactField.value = '';
    pageField.value = window.location.href;
    submitBtn.disabled = false;
    submitBtn.innerHTML = '<span>&#10148;</span> 提交反馈（将跳转到 GitHub Issue）';
  });

  // 关闭模态框
  function closeFeedback() {
    overlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  closeBtn.addEventListener('click', closeFeedback);
  overlay.addEventListener('click', function(e) {
    if (e.target === overlay) closeFeedback();
  });

  // ESC 键关闭
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && overlay.classList.contains('active')) {
      closeFeedback();
    }
  });

  // 提交反馈
  submitBtn.addEventListener('click', function() {
    var type = typeField.value.trim();
    var desc = descField.value.trim();

    // 验证
    if (!type) {
      typeField.focus();
      typeField.style.borderColor = 'var(--hi-red)';
      setTimeout(function() { typeField.style.borderColor = ''; }, 2000);
      return;
    }
    if (!desc) {
      descField.focus();
      descField.style.borderColor = 'var(--hi-red)';
      setTimeout(function() { descField.style.borderColor = ''; }, 2000);
      return;
    }

    submitBtn.disabled = true;
    submitBtn.innerHTML = '正在跳转...';

    // 构建 GitHub Issue 内容
    var pageUrl = window.location.href;
    var name = nameField.value.trim() || '(未填写)';
    var contact = contactField.value.trim() || '(未填写)';

    var title = '[反馈] ' + type + ' - ' + document.title;

    var body = '## 反馈信息\n\n'
      + '**页面**: ' + pageUrl + '\n\n'
      + '**反馈类型**: ' + type + '\n\n'
      + '**问题描述**:\n' + desc + '\n\n'
      + '---\n'
      + '**提交者**: ' + name + '\n'
      + '**联系方式**: ' + contact + '\n'
      + '**浏览器**: ' + navigator.userAgent + '\n'
      + '**提交时间**: ' + new Date().toLocaleString('zh-CN', { timeZone: 'Asia/Shanghai' });

    // 打开 GitHub Issues 预填页面
    var issueUrl = 'https://github.com/' + GITHUB_REPO + '/issues/new?title='
      + encodeURIComponent(title)
      + '&body='
      + encodeURIComponent(body);

    window.open(issueUrl, '_blank');

    // 显示成功
    formArea.style.display = 'none';
    successArea.classList.add('active');

    // 5 秒后自动关闭
    setTimeout(function() {
      closeFeedback();
    }, 5000);
  });
});