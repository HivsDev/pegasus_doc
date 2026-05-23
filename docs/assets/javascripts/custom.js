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

  // ========== 布局优化：首页右侧目录合并到左侧 ==========

  // 防抖：避免 MutationObserver 频繁触发导致重复执行
  var tocRenderTimer = null;
  var tocIsRendering = false;
  var tocLastRunPath = '';
  var tocLastRunTime = 0;

  function setupHomepageLayout() {
    var path = window.location.pathname.replace(/\/+$/, '');
    var isHomepage = path === '/pegasus_doc'
      || path === '/pegasus_doc/index.html'
      || path === ''
      || path === '/'
      || path === '/index.html';

    if (!isHomepage) {
      // 非首页：清除 body class，移除旧 TOC
      document.body.classList.remove('homepage');
      var oldTitle = document.querySelector('.cloned-homepage-toc-title');
      if (oldTitle) oldTitle.remove();
      var oldList = document.querySelector('.cloned-homepage-toc-list');
      if (oldList) oldList.remove();
      return;
    }

    // 同页面且距上次执行不足 100ms，跳过（防抖）
    if (tocLastRunPath === path && (Date.now() - tocLastRunTime) < 100) {
      return;
    }

    // 正在渲染中，跳过（防重入）
    if (tocIsRendering) {
      return;
    }

    document.body.classList.add('homepage');

    // 清除之前 pending 的定时器，避免旧定时器覆盖新结果
    if (tocRenderTimer !== null) {
      clearTimeout(tocRenderTimer);
    }

    tocRenderTimer = setTimeout(function() {
      tocRenderTimer = null;
      tocIsRendering = true;

      var leftInner = document.querySelector('.md-sidebar--primary .md-sidebar__inner');
      var contentArea = document.querySelector('.md-content__inner');

      if (!leftInner || !contentArea) {
        tocIsRendering = false;
        // 元素未就绪，稍后重试
        tocRenderTimer = setTimeout(function() {
          tocRenderTimer = null;
          tocIsRendering = false;
          setupHomepageLayout();
        }, 300);
        return;
      }

      // 清除之前生成的目录（防止重复）
      var oldTitle = leftInner.querySelector('.cloned-homepage-toc-title');
      if (oldTitle) oldTitle.remove();
      var oldList = leftInner.querySelector('.cloned-homepage-toc-list');
      if (oldList) oldList.remove();

      // 从页面内容中提取 h2/h3 标题，生成纯链接目录
      var headings = contentArea.querySelectorAll('h2, h3');
      var items = [];
      headings.forEach(function(h) {
        var id = h.id || (h.querySelector('[id]') ? h.querySelector('[id]').id : null);
        if (id && id.length > 0) {
          // 获取纯净的标题文字（去掉 MkDocs 自动添加的 ¶ permalink 符号）
          var hClone = h.cloneNode(true);
          var perm = hClone.querySelector('.headerlink');
          if (perm) perm.remove();
          var cleanText = hClone.textContent.trim();
          items.push({ id: id, text: cleanText, tag: h.tagName });
        }
      });

      if (items.length > 0) {
        // 分隔标题
        var tocTitle = document.createElement('div');
        tocTitle.className = 'cloned-homepage-toc-title';
        tocTitle.textContent = '📑 本页目录';
        leftInner.appendChild(tocTitle);

        // 生成目录列表
        var list = document.createElement('ul');
        list.className = 'cloned-homepage-toc-list';

        items.forEach(function(item) {
          var li = document.createElement('li');
          li.className = 'cloned-homepage-toc-item';
          if (item.tag === 'H3') {
            li.classList.add('toc-level-h3');
          }

          var link = document.createElement('a');
          link.href = '#' + item.id;
          link.className = 'cloned-homepage-toc-link';
          link.textContent = item.text;

          // 自定义点击处理：绕过 MkDocs 即时导航，平滑滚动到目标
          link.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            var target = document.getElementById(item.id);
            if (target) {
              target.scrollIntoView({ behavior: 'smooth', block: 'start' });
              history.pushState(null, '', '#' + item.id);
            }
          });

          li.appendChild(link);
          list.appendChild(li);
        });

        leftInner.appendChild(list);
      }

      // 隐藏右侧栏
      var rightSidebar = document.querySelector('.md-sidebar--secondary');
      if (rightSidebar) {
        rightSidebar.style.display = 'none';
        rightSidebar.setAttribute('hidden', '');
      }

      tocIsRendering = false;
      tocLastRunPath = path;
      tocLastRunTime = Date.now();
    }, 200);
  }

  // 初次加载执行
  setupHomepageLayout();

  // 监听 MkDocs Material 即时导航后的内容更新（MutationObserver 比 locationchange 更可靠）
  var mdContent = document.querySelector('.md-content');
  if (mdContent) {
    var contentObserver = new MutationObserver(function() {
      // 路由变化时重置状态，确保重新渲染
      tocLastRunPath = '';
      setupHomepageLayout();
    });
    contentObserver.observe(mdContent, { childList: true, subtree: true });
  }

  // 备选：监听浏览器前进/后退
  window.addEventListener('popstate', function() {
    tocLastRunPath = '';
    setupHomepageLayout();
  });

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