<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Budget Tracker</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0a0f;
    --surface: #13131a;
    --surface2: #1c1c28;
    --border: #2a2a3d;
    --income: #00e5a0;
    --expense: #ff4d6d;
    --balance: #7c6aff;
    --text: #e8e8f0;
    --muted: #6b6b8a;
    --accent: #00e5a0;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Syne', sans-serif;
    min-height: 100vh;
    padding: 2rem 1rem;
    background-image:
      radial-gradient(ellipse 60% 40% at 80% 10%, rgba(124,106,255,0.08) 0%, transparent 60%),
      radial-gradient(ellipse 40% 30% at 10% 80%, rgba(0,229,160,0.06) 0%, transparent 50%);
  }

  .container {
    max-width: 480px;
    margin: 0 auto;
  }

  header {
    margin-bottom: 2rem;
    animation: fadeDown 0.5s ease;
  }

  header h1 {
    font-size: 1.8rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    background: linear-gradient(135deg, #fff 30%, var(--balance));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  header p {
    color: var(--muted);
    font-size: 0.85rem;
    margin-top: 0.3rem;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.05em;
  }

  /* Summary cards */
  .summary {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 0.75rem;
    margin-bottom: 2rem;
    animation: fadeUp 0.5s ease 0.1s both;
  }

  .card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1rem 0.8rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s;
  }

  .card:hover { transform: translateY(-2px); }

  .card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    border-radius: 16px 16px 0 0;
  }

  .card.income::before { background: var(--income); }
  .card.expense::before { background: var(--expense); }
  .card.balance::before { background: var(--balance); }

  .card-icon { font-size: 1.2rem; margin-bottom: 0.4rem; }

  .card-label {
    font-size: 0.65rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-family: 'JetBrains Mono', monospace;
  }

  .card-value {
    font-size: 1rem;
    font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
    margin-top: 0.3rem;
    letter-spacing: -0.02em;
  }

  .card.income .card-value { color: var(--income); }
  .card.expense .card-value { color: var(--expense); }
  .card.balance .card-value { color: var(--balance); }

  /* Menu */
  .menu {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    animation: fadeUp 0.5s ease 0.2s both;
  }

  .menu-title {
    font-size: 0.7rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-family: 'JetBrains Mono', monospace;
    margin-bottom: 1rem;
  }

  .menu-buttons {
    display: flex;
    flex-direction: column;
    gap: 0.6rem;
  }

  .menu-btn {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 0.9rem 1.1rem;
    color: var(--text);
    font-family: 'Syne', sans-serif;
    font-size: 0.9rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    text-align: left;
    width: 100%;
  }

  .menu-btn:hover {
    background: #22223a;
    border-color: #44446a;
    transform: translateX(4px);
  }

  .menu-btn:active { transform: translateX(2px) scale(0.99); }

  .menu-btn .num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: var(--muted);
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 0.15rem 0.45rem;
    min-width: 26px;
    text-align: center;
  }

  .menu-btn.btn-income { border-left: 3px solid var(--income); }
  .menu-btn.btn-expense { border-left: 3px solid var(--expense); }
  .menu-btn.btn-exit { border-left: 3px solid var(--muted); }

  /* Form panel */
  .form-panel {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    display: none;
    animation: slideIn 0.3s ease;
  }

  .form-panel.visible { display: block; }

  .form-panel h2 {
    font-size: 1rem;
    font-weight: 700;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .form-group {
    margin-bottom: 1rem;
  }

  label {
    display: block;
    font-size: 0.72rem;
    color: var(--muted);
    font-family: 'JetBrains Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.5rem;
  }

  input {
    width: 100%;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 0.75rem 1rem;
    color: var(--text);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.95rem;
    outline: none;
    transition: border-color 0.2s;
  }

  input:focus { border-color: var(--accent); }
  input::placeholder { color: var(--muted); }

  .form-actions {
    display: flex;
    gap: 0.6rem;
    margin-top: 1.2rem;
  }

  .btn-submit {
    flex: 1;
    padding: 0.8rem;
    border: none;
    border-radius: 10px;
    font-family: 'Syne', sans-serif;
    font-size: 0.9rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
    letter-spacing: 0.02em;
  }

  .btn-submit.income-submit {
    background: var(--income);
    color: #000;
  }

  .btn-submit.expense-submit {
    background: var(--expense);
    color: #fff;
  }

  .btn-submit:hover { opacity: 0.88; transform: translateY(-1px); }

  .btn-cancel {
    padding: 0.8rem 1.2rem;
    background: transparent;
    border: 1px solid var(--border);
    border-radius: 10px;
    color: var(--muted);
    font-family: 'Syne', sans-serif;
    font-size: 0.9rem;
    cursor: pointer;
    transition: all 0.2s;
  }

  .btn-cancel:hover { border-color: #44446a; color: var(--text); }

  /* Toast */
  .toast {
    position: fixed;
    bottom: 2rem;
    left: 50%;
    transform: translateX(-50%) translateY(100px);
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 0.75rem 1.4rem;
    font-size: 0.88rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    transition: transform 0.35s cubic-bezier(0.34,1.56,0.64,1), opacity 0.35s;
    z-index: 100;
    white-space: nowrap;
    opacity: 0;
  }

  .toast.show {
    transform: translateX(-50%) translateY(0);
    opacity: 1;
  }

  /* Transactions */
  .tx-panel {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 1.5rem;
    animation: fadeUp 0.5s ease 0.3s both;
  }

  .tx-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  }

  .tx-header h3 {
    font-size: 0.72rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-family: 'JetBrains Mono', monospace;
  }

  .tx-count {
    font-size: 0.72rem;
    color: var(--muted);
    font-family: 'JetBrains Mono', monospace;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 0.2rem 0.7rem;
  }

  .tx-list { display: flex; flex-direction: column; gap: 0.5rem; }

  .tx-empty {
    text-align: center;
    padding: 2rem 0;
    color: var(--muted);
    font-size: 0.85rem;
    font-family: 'JetBrains Mono', monospace;
  }

  .tx-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--surface2);
    border-radius: 10px;
    padding: 0.7rem 0.9rem;
    border: 1px solid var(--border);
    animation: slideIn 0.25s ease;
  }

  .tx-left { display: flex; align-items: center; gap: 0.6rem; }

  .tx-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
  }

  .tx-dot.income { background: var(--income); }
  .tx-dot.expense { background: var(--expense); }

  .tx-category {
    font-size: 0.85rem;
    font-weight: 600;
  }

  .tx-type {
    font-size: 0.68rem;
    color: var(--muted);
    font-family: 'JetBrains Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 0.06em;
  }

  .tx-amount {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.9rem;
    font-weight: 500;
  }

  .tx-amount.income { color: var(--income); }
  .tx-amount.expense { color: var(--expense); }

  @keyframes fadeDown {
    from { opacity: 0; transform: translateY(-16px); }
    to { opacity: 1; transform: translateY(0); }
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to { opacity: 1; transform: translateY(0); }
  }

  @keyframes slideIn {
    from { opacity: 0; transform: translateX(-10px); }
    to { opacity: 1; transform: translateX(0); }
  }
</style>
</head>
<body>
<div class="container">

  <header>
    <h1>Budget Tracker</h1>
    <p>// personal finance terminal</p>
  </header>

  <!-- Summary Cards (same as option 3 in Python) -->
  <div class="summary">
    <div class="card income">
      <div class="card-icon">💚</div>
      <div class="card-label">Income</div>
      <div class="card-value" id="totalIncome">₹0.00</div>
    </div>
    <div class="card expense">
      <div class="card-icon">🔴</div>
      <div class="card-label">Expenses</div>
      <div class="card-value" id="totalExpense">₹0.00</div>
    </div>
    <div class="card balance">
      <div class="card-icon">💰</div>
      <div class="card-label">Balance</div>
      <div class="card-value" id="totalBalance">₹0.00</div>
    </div>
  </div>

  <!-- Menu (mirrors the while True menu) -->
  <div class="menu">
    <div class="menu-title">// menu</div>
    <div class="menu-buttons">
      <button class="menu-btn btn-income" onclick="openForm('income')">
        <span class="num">1</span>
        Add Income
      </button>
      <button class="menu-btn btn-expense" onclick="openForm('expense')">
        <span class="num">2</span>
        Add Transaction (Expense)
      </button>
      <button class="menu-btn btn-exit" onclick="exitApp()">
        <span class="num">4</span>
        Exit
      </button>
    </div>
  </div>

  <!-- Form Panel (shown when 1 or 2 is clicked) -->
  <div class="form-panel" id="formPanel">
    <h2 id="formTitle">Add Income</h2>
    <div class="form-group">
      <label>Amount (₹)</label>
      <input type="number" id="amountInput" placeholder="0.00" min="0" step="0.01">
    </div>
    <div class="form-group">
      <label>Category</label>
      <input type="text" id="categoryInput" placeholder="e.g. Salary, Food, Rent...">
    </div>
    <div class="form-actions">
      <button class="btn-submit" id="submitBtn" onclick="addTransaction()">✅ Add</button>
      <button class="btn-cancel" onclick="closeForm()">Cancel</button>
    </div>
  </div>

  <!-- Transaction List (View Summary — option 3) -->
  <div class="tx-panel">
    <div class="tx-header">
      <h3>// transactions</h3>
      <span class="tx-count" id="txCount">0 entries</span>
    </div>
    <div class="tx-list" id="txList">
      <div class="tx-empty">No transactions yet.</div>
    </div>
  </div>

</div>

<!-- Toast notification -->
<div class="toast" id="toast"></div>

<script>
  // === Python logic ported to JS (same logic, no changes to original rules) ===
  const transactions = [];   // same as Python: transactions = []

  let currentType = 'income';

  function openForm(type) {
    currentType = type;
    const panel = document.getElementById('formPanel');
    const title = document.getElementById('formTitle');
    const btn   = document.getElementById('submitBtn');
    title.textContent = type === 'income' ? '💚 Add Income' : '🔴 Add Transaction (Expense)';
    btn.className = 'btn-submit ' + (type === 'income' ? 'income-submit' : 'expense-submit');
    btn.textContent = type === 'income' ? '✅ Add Income' : '✅ Add Expense';
    document.getElementById('amountInput').value = '';
    document.getElementById('categoryInput').value = '';
    panel.classList.add('visible');
    document.getElementById('amountInput').focus();
  }

  function closeForm() {
    document.getElementById('formPanel').classList.remove('visible');
  }

  function addTransaction() {
    const amountRaw = document.getElementById('amountInput').value.trim();
    const category  = document.getElementById('categoryInput').value.trim();

    // === mirrors Python: try: amount = float(input("Amount (₹): ")) ===
    const amount = parseFloat(amountRaw);
    if (isNaN(amount) || amount <= 0) {
      showToast('❌ Enter a valid number!');
      return;
    }
    if (!category) {
      showToast('❌ Enter a category!');
      return;
    }

    // === mirrors Python: transactions.append({...}) ===
    transactions.push({ type: currentType, amount, category });

    showToast(`✅ Added ${currentType} of ₹${amount.toFixed(2)}`);
    closeForm();
    renderAll();
  }

  function renderAll() {
    // === mirrors Python option 3: View Summary ===
    const income   = transactions.filter(t => t.type === 'income').reduce((s,t) => s + t.amount, 0);
    const expenses = transactions.filter(t => t.type === 'expense').reduce((s,t) => s + t.amount, 0);
    const balance  = income - expenses;

    document.getElementById('totalIncome').textContent  = `₹${income.toFixed(2)}`;
    document.getElementById('totalExpense').textContent = `₹${expenses.toFixed(2)}`;
    document.getElementById('totalBalance').textContent = `₹${balance.toFixed(2)}`;
    document.getElementById('totalBalance').style.color = balance < 0 ? 'var(--expense)' : 'var(--balance)';

    // Transaction list
    const list = document.getElementById('txList');
    const countEl = document.getElementById('txCount');
    countEl.textContent = `${transactions.length} ${transactions.length === 1 ? 'entry' : 'entries'}`;

    if (transactions.length === 0) {
      list.innerHTML = '<div class="tx-empty">No transactions yet.</div>';
      return;
    }

    list.innerHTML = [...transactions].reverse().map(t => `
      <div class="tx-item">
        <div class="tx-left">
          <div class="tx-dot ${t.type}"></div>
          <div>
            <div class="tx-category">${t.category}</div>
            <div class="tx-type">${t.type}</div>
          </div>
        </div>
        <div class="tx-amount ${t.type}">
          ${t.type === 'income' ? '+' : '-'}₹${t.amount.toFixed(2)}
        </div>
      </div>
    `).join('');
  }

  function exitApp() {
    showToast('Good Bye! 👋');
    setTimeout(() => {
      document.querySelector('.container').style.transition = 'opacity 0.5s';
      document.querySelector('.container').style.opacity = '0';
    }, 800);
  }

  function showToast(msg) {
    const t = document.getElementById('toast');
    t.textContent = msg;
    t.classList.add('show');
    clearTimeout(t._timer);
    t._timer = setTimeout(() => t.classList.remove('show'), 2500);
  }

  // Allow Enter key to submit form
  document.addEventListener('keydown', e => {
    if (e.key === 'Enter' && document.getElementById('formPanel').classList.contains('visible')) {
      addTransaction();
    }
    if (e.key === 'Escape') closeForm();
  });
</script>
</body>
</html>
