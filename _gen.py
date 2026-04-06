#!/usr/bin/env python3
"""Generate all remaining Georgia city/suburb pages."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

CSS = """*{margin:0;padding:0;box-sizing:border-box}body{background:#0d1117;color:#c9d1d9;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;line-height:1.6}a{color:#58a6ff;text-decoration:none}a:hover{text-decoration:underline}.container{max-width:1100px;margin:0 auto;padding:0 20px}nav{background:#161b22;border-bottom:1px solid #30363d;padding:12px 0;position:sticky;top:0;z-index:100}nav .container{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px}nav .brand{color:#f0f6fc;font-weight:700;font-size:1.1rem}nav .links{display:flex;gap:16px;flex-wrap:wrap}nav .links a{color:#8b949e;font-size:0.9rem}nav .links a:hover{color:#58a6ff}.hero{padding:60px 0 40px;text-align:center;border-bottom:1px solid #30363d}.hero h1{color:#f0f6fc;font-size:2.4rem;margin-bottom:12px}.hero .subtitle{color:#8b949e;font-size:1.15rem;max-width:700px;margin:0 auto 24px}.hero .alert{background:#f8514920;border:1px solid #f85149;border-radius:8px;padding:16px 24px;display:inline-block;color:#f85149;font-weight:600;font-size:1.05rem}.stats-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;padding:32px 0}.stat-card{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:24px;text-align:center}.stat-card .number{color:#58a6ff;font-size:2.2rem;font-weight:700}.stat-card .label{color:#8b949e;font-size:0.9rem;margin-top:4px}.stat-card.danger .number{color:#f85149}section{padding:40px 0;border-bottom:1px solid #21262d}h2{color:#f0f6fc;font-size:1.8rem;margin-bottom:16px}h3{color:#f0f6fc;font-size:1.3rem;margin-bottom:12px}p{margin-bottom:16px}.card{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:24px;margin-bottom:20px}.faq-item{background:#161b22;border:1px solid #30363d;border-radius:8px;margin-bottom:12px;overflow:hidden}.faq-item summary{padding:16px 20px;cursor:pointer;color:#f0f6fc;font-weight:600;list-style:none;display:flex;justify-content:space-between;align-items:center}.faq-item summary::after{content:"+";color:#58a6ff;font-size:1.3rem;font-weight:700}.faq-item[open] summary::after{content:"-"}.faq-item .answer{padding:0 20px 16px;color:#c9d1d9}.network{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:24px;margin:32px 0}.network h3{margin-bottom:12px}.network-links{display:flex;flex-wrap:wrap;gap:8px}.network-links a{background:#21262d;padding:6px 14px;border-radius:16px;font-size:0.85rem;border:1px solid #30363d}.network-links a:hover{border-color:#58a6ff;background:#161b22}footer{background:#161b22;border-top:1px solid #30363d;padding:32px 0;text-align:center;color:#8b949e;font-size:0.85rem}footer a{color:#58a6ff}footer p{margin-bottom:8px}.cta{display:inline-block;background:#238636;color:#fff;padding:12px 28px;border-radius:6px;font-weight:600;margin-top:12px;font-size:1rem}.cta:hover{background:#2ea043;text-decoration:none}ul,ol{margin:12px 0 12px 24px}li{margin-bottom:6px}table{width:100%;border-collapse:collapse;margin:16px 0}th,td{padding:10px 14px;text-align:left;border-bottom:1px solid #30363d}th{color:#f0f6fc;background:#161b22;font-weight:600}td{color:#c9d1d9}@media(max-width:768px){.hero h1{font-size:1.7rem}.stats-row{grid-template-columns:1fr 1fr}}@media(max-width:480px){.stats-row{grid-template-columns:1fr}}"""

GA4 = '<script async src="https://www.googletagmanager.com/gtag/js?id=G-CSBPNV4NKL"></script>\n<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag(\'js\',new Date());gtag(\'config\',\'G-CSBPNV4NKL\');gtag(\'config\',\'G-053Z64N82F\');gtag(\'config\',\'G-FTWLM223G7\');</script>'

FOOTER = '<footer><div class="container"><p>An <a href="https://openbankruptcyproject.org">Open Bankruptcy Project</a> resource</p><p>Data sourced from the Federal Judicial Center Integrated Database (2008--2024).</p><p>This site provides general information, not legal advice. Consult a qualified attorney for your specific situation.</p><p>&copy; 2026 Open Bankruptcy Project. <a href="https://github.com/openbankruptcyproject">GitHub</a></p></div></footer><script src="/btn-engage.js"></script>'

OBP = '<div class="network"><h3>Open Bankruptcy Project Network</h3><div class="network-links"><a href="https://openbankruptcyproject.org">OBP Home</a><a href="https://1328f.com">1328(f) Screener</a><a href="https://chapter7vs13.org">Ch. 7 vs 13</a><a href="https://automaticstay.org">Automatic Stay</a><a href="https://341meeting.org">341 Meeting</a><a href="https://bankruptcymeanstest.org">Means Test</a><a href="https://howmuchdoesbankruptcycost.com">Cost Guide</a><a href="https://bankruptcydismissed.com">Dismissed?</a><a href="https://filebankruptcyagain.com">File Again?</a><a href="https://howtofilebankruptcy.org">How to File</a></div></div>'

ATL_NAV = '<nav><div class="container"><a href="/atlanta/" class="brand">Atlanta Bankruptcy Guide</a><div class="links"><a href="/">Georgia</a><a href="/atlanta/">Atlanta</a><a href="/atlanta/chapter-7.html">Chapter 7</a><a href="/atlanta/chapter-13.html">Chapter 13</a><a href="/atlanta/exemptions.html">Exemptions</a><a href="/atlanta/cost.html">Cost</a><a href="/atlanta/faq.html">FAQ</a></div></div></nav>'

def write_page(rel_path, title, desc, canonical, faq_pairs, breadcrumbs, nav, body):
    path = os.path.join(BASE, rel_path)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    bc = ','.join(f'{{"@type":"ListItem","position":{i+1},"name":"{n}","item":"{u}"}}' for i,(n,u) in enumerate(breadcrumbs))
    faq_json = ""
    if faq_pairs:
        entries = ','.join(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}' for q,a in faq_pairs)
        faq_json = f'<script type="application/ld+json">\n{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{entries}]}}\n</script>'

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="canonical" href="{canonical}">
{GA4}
{faq_json}
<script type="application/ld+json">
{{"@context":"https://schema.org","@graph":[{{"@type":"Article","headline":"{title}","description":"{desc}","author":{{"@type":"Organization","name":"Open Bankruptcy Project"}},"publisher":{{"@type":"Organization","name":"Open Bankruptcy Project","url":"https://1328f.org"}},"datePublished":"2026-04-05","dateModified":"2026-04-05","mainEntityOfPage":"{canonical}"}},{{"@type":"BreadcrumbList","itemListElement":[{bc}]}}]}}
</script>
<style>{CSS}</style>
</head>
<body>
{nav}
{body}
{FOOTER}
</body>
</html>"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  OK: {rel_path}")

bc_atl = lambda n,u: [("Georgia","https://georgiabankruptcy.org"),("Atlanta","https://georgiabankruptcy.org/atlanta/"),(n,f"https://georgiabankruptcy.org/atlanta/{u}")]

# ── MEANS TEST ──
write_page("atlanta/means-test.html",
    "Atlanta Bankruptcy Means Test -- Georgia Income Limits 2026",
    "Do you qualify for Chapter 7 in Atlanta? Georgia means test income thresholds, expense deductions, and eligibility calculator for the Northern District.",
    "https://georgiabankruptcy.org/atlanta/means-test.html",
    [("What is the means test for Atlanta bankruptcy?","The means test compares your household income to Georgia median. Below median (about $55,000 single) = automatic Chapter 7 qualification. Above = may still qualify after expense deductions."),
     ("What is Georgia median income for bankruptcy?","Approximately $55,000 single, $70,000 for two, $78,000 for three, $91,000 for four. Updated periodically by the U.S. Trustee.")],
    bc_atl("Means Test","means-test.html"), ATL_NAV,
    f"""<div class="hero"><div class="container">
<h1>The Bankruptcy Means Test in Atlanta</h1>
<p class="subtitle">The means test determines whether you qualify for Chapter 7. Here is how it works and what the current Georgia income thresholds are.</p>
</div></div>
<section><div class="container"><h2>How the Means Test Works</h2><div class="card">
<p>The means test has two parts:</p>
<ol><li><strong>Income comparison:</strong> Your average monthly income over the past 6 months is compared to Georgia's median for your household size. Below median = you pass.</li>
<li><strong>Expense deduction:</strong> If above median, you deduct allowed expenses (housing, transportation, taxes, etc.). If remaining disposable income is low enough, you still qualify.</li></ol>
</div></div></section>
<section><div class="container"><h2>Georgia Median Income (2026 approximate)</h2><div class="card">
<table><tr><th>Household Size</th><th>Annual Median</th><th>Monthly</th></tr>
<tr><td>1 person</td><td>$55,000</td><td>$4,583</td></tr>
<tr><td>2 people</td><td>$70,000</td><td>$5,833</td></tr>
<tr><td>3 people</td><td>$78,000</td><td>$6,500</td></tr>
<tr><td>4 people</td><td>$91,000</td><td>$7,583</td></tr>
<tr><td>Each additional</td><td>Add ~$9,000</td><td>Add ~$750</td></tr></table>
<p style="margin-top:12px;color:#8b949e;font-size:0.9rem">Current data: <a href="https://www.justice.gov/ust/means-testing" target="_blank" rel="noopener">justice.gov/ust/means-testing</a></p>
</div></div></section>
<section><div class="container"><h2>What Counts as Income?</h2><div class="card">
<p>Average gross income over the 6 months before filing:</p>
<ul><li>Wages, salary, tips, bonuses</li><li>Net business income</li><li>Rental income</li><li>Pension and retirement income</li><li>Regular contributions from others</li></ul>
<p><strong>Not included:</strong> Social Security benefits, certain disability payments.</p>
</div></div></section>
<section><div class="container"><h2>Allowed Expense Deductions</h2><div class="card">
<ul><li><strong>IRS National Standards:</strong> Food, clothing, personal care</li>
<li><strong>IRS Local Standards:</strong> Housing/utilities (by county), transportation</li>
<li><strong>Actual expenses:</strong> Taxes, health insurance, child care</li>
<li><strong>Secured debt:</strong> Mortgage, car payments</li></ul>
<p>Atlanta-area housing costs (Fulton, DeKalb, Cobb, Gwinnett) are among Georgia's highest, yielding higher allowed deductions.</p>
</div></div></section>
<section><div class="container"><h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>What if I fail the means test?</summary><div class="answer"><p>You can file Chapter 13 instead (no income limit). Or re-examine expenses for additional deductions.</p></div></details>
<details class="faq-item"><summary>Does my spouse's income count?</summary><div class="answer"><p>Joint filers: both incomes count. Individual filers: spouse income is included but their expenses are deducted too.</p></div></details>
<details class="faq-item"><summary>What if I recently lost my job?</summary><div class="answer"><p>The test uses 6-month averages. Waiting a few months may help if higher-income months drop off.</p></div></details>
</div></section>
<div class="container"><div style="text-align:center;padding:40px 0"><a href="https://meanstest.org" class="cta">Means Test Calculator</a></div>{OBP}</div>""")

# ── AUTOMATIC STAY ──
write_page("atlanta/automatic-stay.html",
    "The Automatic Stay in Atlanta Bankruptcy -- How It Protects You",
    "How the automatic stay protects Atlanta filers from foreclosure, repossession, garnishment, and collections the moment you file in N.D. Ga.",
    "https://georgiabankruptcy.org/atlanta/automatic-stay.html",
    [("What does the automatic stay stop?","Foreclosure, repossession, wage garnishment, bank levies, lawsuits, utility shutoffs, and collection calls. Takes effect immediately when your petition is filed."),
     ("How long does the automatic stay last?","Chapter 7: until case closure (3-4 months). Chapter 13: duration of 3-5 year plan. Limited to 30 days if a prior case was dismissed within the past year.")],
    bc_atl("Automatic Stay","automatic-stay.html"), ATL_NAV,
    f"""<div class="hero"><div class="container">
<h1>The Automatic Stay in Atlanta Bankruptcy</h1>
<p class="subtitle">The moment you file, the automatic stay kicks in -- a federal order that immediately stops creditors from taking action against you.</p>
</div></div>
<section><div class="container"><h2>What the Automatic Stay Stops</h2><div class="card">
<table><tr><th>Action</th><th>Stopped?</th><th>Details</th></tr>
<tr><td>Foreclosure</td><td>Yes</td><td>Critical -- Georgia non-judicial foreclosure in 60 days</td></tr>
<tr><td>Repossession</td><td>Yes</td><td>Lender cannot take your car</td></tr>
<tr><td>Wage garnishment</td><td>Yes</td><td>Employer stops withholding after notice</td></tr>
<tr><td>Bank levy</td><td>Yes</td><td>Creditors cannot seize bank funds</td></tr>
<tr><td>Collection calls</td><td>Yes</td><td>Violators face contempt</td></tr>
<tr><td>Lawsuits</td><td>Yes</td><td>Most civil suits paused</td></tr>
<tr><td>Utility disconnection</td><td>20 days</td><td>Must pay deposit after</td></tr>
<tr><td>Eviction</td><td>Limited</td><td>May not stop if landlord has judgment</td></tr>
<tr><td>Criminal cases</td><td>No</td><td>Not affected</td></tr>
<tr><td>Child support</td><td>No</td><td>Domestic support continues</td></tr></table>
</div></div></section>
<section><div class="container"><h2>Why It Matters in Georgia</h2><div class="card">
<p>Georgia is a <strong>non-judicial foreclosure state</strong> -- foreclosure in as few as <strong>60 days</strong>. The automatic stay takes effect <strong>immediately</strong> when your petition is filed at 75 Ted Turner Dr SW, Atlanta, GA 30303.</p>
</div></div></section>
<section><div class="container"><h2>Limitations</h2><div class="card">
<ul><li><strong>One prior dismissal in past year:</strong> Stay expires after 30 days unless you motion to extend</li>
<li><strong>Two+ prior dismissals:</strong> Stay does not take effect unless you motion for it</li></ul>
<p>With N.D. Ga.'s 44.8% prior filer rate, many debtors face these limitations. Discuss with an attorney before filing.</p>
</div></div></section>
<section><div class="container"><h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>What does the stay stop?</summary><div class="answer"><p>Foreclosure, repossession, garnishment, bank levies, lawsuits, collections, and utility disconnection.</p></div></details>
<details class="faq-item"><summary>How long does it last?</summary><div class="answer"><p>Ch. 7: 3-4 months. Ch. 13: 3-5 years. Limited if prior case dismissed within 1 year.</p></div></details>
<details class="faq-item"><summary>What if a creditor violates it?</summary><div class="answer"><p>They face contempt of court and may owe you damages plus attorney fees.</p></div></details>
</div></section>
<div class="container">{OBP}</div>""")

# ── KEEP YOUR CAR ──
write_page("atlanta/keep-your-car.html",
    "Keep Your Car in Atlanta Bankruptcy -- Georgia Vehicle Exemption Guide",
    "How to keep your car when filing bankruptcy in Atlanta. Georgia $5,000 vehicle exemption, reaffirmation, redemption, and cramdown options explained.",
    "https://georgiabankruptcy.org/atlanta/keep-your-car.html",
    [("Can I keep my car in Atlanta bankruptcy?","Usually yes. Georgia protects $5,000 of vehicle equity. Wildcard adds up to $5,600 more. If you owe more than the car is worth, it is fully protected."),
     ("What is a cramdown?","If you have owned your car 910+ days, Chapter 13 can reduce the loan to current market value. The excess becomes unsecured debt.")],
    bc_atl("Keep Your Car","keep-your-car.html"), ATL_NAV,
    f"""<div class="hero"><div class="container">
<h1>How to Keep Your Car in Atlanta Bankruptcy</h1>
<p class="subtitle">Georgia's $5,000 vehicle exemption protects most cars. Here are all your options for keeping your vehicle when filing in N.D. Ga.</p>
</div></div>
<section><div class="container"><h2>Georgia Vehicle Exemption</h2><div class="card">
<p>Georgia exempts <strong>$5,000</strong> of equity in one motor vehicle. Equity = market value minus loan balance.</p>
<ul><li>Car worth $15,000, owe $14,000 = $1,000 equity. <strong>Fully protected.</strong></li>
<li>Car worth $8,000, paid off = $8,000 equity. $5,000 protected; wildcard covers rest.</li>
<li>Car worth $10,000, owe $12,000 = no equity. <strong>Fully protected.</strong></li></ul>
</div></div></section>
<section><div class="container"><h2>Wildcard Boost</h2><div class="card">
<p>Georgia wildcard: <strong>$600</strong> for any property + up to <strong>$5,000</strong> unused homestead. Renters get $5,600 wildcard. Combined: up to <strong>$10,600</strong> vehicle protection.</p>
</div></div></section>
<section><div class="container"><h2>Chapter 7 Options</h2><div class="card">
<h3>1. Reaffirmation</h3><p>Continue making payments after bankruptcy. Keep the car and loan.</p>
<h3>2. Redemption</h3><p>Pay current market value in a lump sum. Works if car worth less than owed.</p>
<h3>3. Surrender</h3><p>Return the car. Remaining balance is discharged.</p>
</div></div></section>
<section><div class="container"><h2>Chapter 13 Cramdown</h2><div class="card">
<p>Owned car <strong>910+ days</strong>? Chapter 13 can reduce the loan to current value. Example: owe $18,000 on car worth $10,000 -- secured claim becomes $10,000, remainder is unsecured.</p>
<p style="color:#f85149">Remember: N.D. Ga. has 72.9% Chapter 13 dismissal rate. Ensure you can sustain payments.</p>
</div></div></section>
<section><div class="container"><h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>Can I keep my car?</summary><div class="answer"><p>Usually yes. $5,000 exemption + $5,600 wildcard (if renting) = up to $10,600 protected.</p></div></details>
<details class="faq-item"><summary>What if it was already repossessed?</summary><div class="answer"><p>File quickly. The automatic stay may require the lender to return the vehicle.</p></div></details>
</div></section>
<div class="container">{OBP}</div>""")

# ── KEEP YOUR HOUSE ──
write_page("atlanta/keep-your-house.html",
    "Keep Your House in Atlanta Bankruptcy -- Stop Foreclosure in Georgia",
    "How to save your home from foreclosure in Atlanta. Georgia $21,500 homestead exemption, Chapter 13 mortgage cure, non-judicial foreclosure defense.",
    "https://georgiabankruptcy.org/atlanta/keep-your-house.html",
    [("Can bankruptcy stop foreclosure in Atlanta?","Yes. The automatic stay immediately halts foreclosure. Georgia allows non-judicial foreclosure in 60 days, making the stay critical."),
     ("How does Chapter 13 save my home?","Chapter 13 lets you catch up on missed payments over 3-5 years while keeping your home. You resume regular mortgage payments and pay arrears through the plan.")],
    bc_atl("Keep Your House","keep-your-house.html"), ATL_NAV,
    f"""<div class="hero"><div class="container">
<h1>How to Keep Your House in Atlanta Bankruptcy</h1>
<p class="subtitle">Georgia allows non-judicial foreclosure in 60 days. Bankruptcy can stop it. Here is how to protect your home.</p>
</div></div>
<section><div class="container"><h2>Georgia Homestead Exemption</h2><div class="card">
<p><strong>$21,500</strong> of equity protected ($43,000 joint). Equity = market value minus mortgage.</p>
<p>Example: Home worth $300,000, mortgage $285,000, equity $15,000 -- fully protected.</p>
</div></div></section>
<section><div class="container"><h2>Stopping Foreclosure</h2><div class="card">
<p>Georgia is a <strong>non-judicial foreclosure state</strong> -- foreclosure in as few as 60 days:</p>
<ul><li>30 days written notice to borrower</li><li>4 weeks newspaper advertisement</li><li>Sale on first Tuesday of the month</li></ul>
<p>Filing bankruptcy triggers the <a href="https://automaticstay.org">automatic stay</a>, stopping the sale <strong>immediately</strong>.</p>
</div></div></section>
<section><div class="container"><h2>Chapter 13: Catch Up on Payments</h2><div class="card">
<ol><li>Automatic stay stops foreclosure</li><li>Resume regular mortgage payments</li><li>Arrears spread across 3-5 year plan</li><li>Lender cannot foreclose while you are current</li></ol>
<p style="color:#f85149"><strong>Warning:</strong> 72.9% of N.D. Ga. Chapter 13 cases are dismissed. Budget carefully.</p>
</div></div></section>
<section><div class="container"><h2>Chapter 7 and Your Home</h2><div class="card">
<p>Chapter 7 delays foreclosure 3-4 months but does not cure missed payments. Best if you are current on the mortgage and want to eliminate other debts, or if you plan to surrender.</p>
</div></div></section>
<section><div class="container"><h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>Can bankruptcy stop foreclosure?</summary><div class="answer"><p>Yes. Automatic stay halts it immediately. Chapter 13 lets you catch up over 3-5 years.</p></div></details>
<details class="faq-item"><summary>How fast can Georgia foreclose?</summary><div class="answer"><p>As few as 60 days. Non-judicial process, sales on first Tuesday of the month.</p></div></details>
</div></section>
<div class="container">{OBP}</div>""")

# ── MEDICAL DEBT ──
write_page("atlanta/medical-debt.html",
    "Medical Debt and Bankruptcy in Atlanta, GA -- Your Options",
    "How bankruptcy eliminates medical debt in Atlanta. Chapter 7 discharges medical bills completely. Chapter 13 reduces them to a fraction.",
    "https://georgiabankruptcy.org/atlanta/medical-debt.html",
    [("Does bankruptcy eliminate medical debt?","Yes. Medical debt is unsecured and fully dischargeable in Chapter 7. In Chapter 13, you typically pay 0-10% of medical bills through your plan."),
     ("Can a hospital sue me in Georgia?","Yes. Medical providers can sue, garnish wages, and place liens. Statute of limitations is 6 years. Bankruptcy stops all collection.")],
    bc_atl("Medical Debt","medical-debt.html"), ATL_NAV,
    f"""<div class="hero"><div class="container">
<h1>Medical Debt and Bankruptcy in Atlanta</h1>
<p class="subtitle">Medical bills are the leading cause of financial hardship. Bankruptcy can eliminate them entirely.</p>
</div></div>
<section><div class="container"><h2>How Bankruptcy Handles Medical Debt</h2><div class="card">
<h3>Chapter 7</h3><p><strong>Eliminates medical debt completely.</strong> Discharge in 3-4 months. Hospitals and collectors cannot contact you again.</p>
<h3>Chapter 13</h3><p>Medical bills are unsecured debt. You pay a percentage (often 0-10%) through your 3-5 year plan. The rest is discharged.</p>
</div></div></section>
<section><div class="container"><h2>Alternatives Before Filing</h2><div class="card">
<ul><li><strong>Hospital charity care:</strong> Most Georgia hospitals have financial assistance programs</li>
<li><strong>Payment plans:</strong> Interest-free arrangements</li>
<li><strong>Negotiation:</strong> Collectors often settle for 20-50 cents on the dollar</li>
<li><strong>Statute of limitations:</strong> 6 years in Georgia</li></ul>
</div></div></section>
<section><div class="container"><h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>Does bankruptcy eliminate medical debt?</summary><div class="answer"><p>Yes. Chapter 7 eliminates it completely. Chapter 13 pays a fraction through your plan.</p></div></details>
<details class="faq-item"><summary>Can a hospital sue me?</summary><div class="answer"><p>Yes. Georgia allows lawsuits, garnishment, and liens for medical debt. Statute of limitations: 6 years. Bankruptcy stops all collection.</p></div></details>
</div></section>
<div class="container">{OBP}</div>""")

# ── 341 MEETING ──
write_page("atlanta/341-meeting.html",
    "The 341 Meeting of Creditors in Atlanta -- What to Expect",
    "What happens at the 341 meeting in Atlanta. Location, questions asked, what to bring, and how to prepare for your meeting at N.D. Ga.",
    "https://georgiabankruptcy.org/atlanta/341-meeting.html",
    [("What happens at the 341 meeting?","A trustee asks questions under oath about your income, expenses, assets, and petition accuracy. Lasts 5-10 minutes. Held ~30 days after filing. Not before a judge."),
     ("Where is the 341 meeting in Atlanta?","At or near the N.D. Ga. courthouse, 75 Ted Turner Dr SW, Atlanta, GA 30303. Some may be by phone/video.")],
    bc_atl("341 Meeting","341-meeting.html"), ATL_NAV,
    f"""<div class="hero"><div class="container">
<h1>The 341 Meeting of Creditors in Atlanta</h1>
<p class="subtitle">A required step in every bankruptcy case. Here is what to expect at the N.D. Ga. courthouse.</p>
</div></div>
<section><div class="container"><h2>What Is the 341 Meeting?</h2><div class="card">
<ul><li><strong>Duration:</strong> 5-10 minutes</li><li><strong>Conducted by:</strong> Court-appointed trustee (not a judge)</li><li><strong>When:</strong> ~30 days after filing</li><li><strong>Where:</strong> N.D. Ga. courthouse, 75 Ted Turner Dr SW, Atlanta, GA 30303</li><li><strong>Format:</strong> In-person, phone, or video</li></ul>
</div></div></section>
<section><div class="container"><h2>What to Bring</h2><div class="card">
<ul><li>Government-issued photo ID</li><li>Proof of Social Security number</li><li>Recent pay stubs (60 days)</li><li>Most recent tax return</li><li>Bank statements (60-90 days)</li><li>Copy of your petition</li></ul>
</div></div></section>
<section><div class="container"><h2>Common Questions</h2><div class="card">
<ol><li>Did you review and sign your petition?</li><li>Is everything true and correct?</li><li>Did you list all assets and debts?</li><li>Have you transferred property in the last 2 years?</li><li>Do you expect inheritance or lawsuit proceeds?</li><li>Are tax filings current?</li></ol>
<p>Answer honestly and briefly. Your attorney will be present.</p>
</div></div></section>
<section><div class="container"><h2>Tips</h2><div class="card">
<ul><li>Arrive early for courthouse security</li><li>Business casual dress</li><li>Answer questions briefly -- do not volunteer extra info</li><li>Be honest -- lying is a federal crime</li></ul>
</div></div></section>
<section><div class="container"><h2>FAQ</h2>
<details class="faq-item"><summary>Do creditors actually show up?</summary><div class="answer"><p>Rarely. In most consumer cases, no creditors attend.</p></div></details>
<details class="faq-item"><summary>What if I cannot attend?</summary><div class="answer"><p>You must attend. Missing it can cause dismissal. Request a continuance for emergencies.</p></div></details>
</div></section>
<div class="container">{OBP}</div>""")

# ── TIMELINE ──
write_page("atlanta/timeline.html",
    "Atlanta Bankruptcy Timeline -- Step by Step for N.D. Ga.",
    "Step-by-step bankruptcy timeline for Atlanta. From credit counseling to discharge for Chapter 7 (3-4 months) and Chapter 13 (3-5 years) in N.D. Ga.",
    "https://georgiabankruptcy.org/atlanta/timeline.html",
    [("How long does Chapter 7 take in Atlanta?","3-4 months. 341 meeting at ~30 days, discharge ~60-90 days after that."),
     ("How long does Chapter 13 take?","3-5 years. Plan confirmed ~45-75 days after filing. Discharge after all payments.")],
    bc_atl("Timeline","timeline.html"), ATL_NAV,
    f"""<div class="hero"><div class="container">
<h1>Atlanta Bankruptcy Timeline</h1>
<p class="subtitle">Step-by-step walkthrough for both Chapter 7 and Chapter 13 in the Northern District of Georgia.</p>
</div></div>
<section><div class="container"><h2>Chapter 7 Timeline (3-4 months)</h2><div class="card">
<table><tr><th>Step</th><th>When</th><th>Details</th></tr>
<tr><td>Credit counseling</td><td>Before filing</td><td>1 hour online, $15-25</td></tr>
<tr><td>File petition</td><td>Day 0</td><td>Automatic stay begins immediately</td></tr>
<tr><td>341 Meeting</td><td>~Day 30</td><td>5-10 min with trustee</td></tr>
<tr><td>Objection deadline</td><td>Day 90</td><td>Creditors: 60 days after 341</td></tr>
<tr><td>Debtor education</td><td>Before discharge</td><td>2 hours online, $10-25</td></tr>
<tr><td>Discharge</td><td>~Day 90-120</td><td>Debts eliminated</td></tr></table>
</div></div></section>
<section><div class="container"><h2>Chapter 13 Timeline (3-5 years)</h2><div class="card">
<table><tr><th>Step</th><th>When</th><th>Details</th></tr>
<tr><td>Credit counseling</td><td>Before filing</td><td>Same as Ch. 7</td></tr>
<tr><td>File petition + plan</td><td>Day 0</td><td>Automatic stay begins</td></tr>
<tr><td>First payment</td><td>Day 30</td><td>Due before confirmation</td></tr>
<tr><td>341 Meeting</td><td>~Day 30</td><td>Same as Ch. 7</td></tr>
<tr><td>Plan confirmation</td><td>~Day 45-75</td><td>Judge reviews plan</td></tr>
<tr><td>Monthly payments</td><td>Ongoing</td><td>3-5 years</td></tr>
<tr><td>Discharge</td><td>After plan</td><td>Remaining debts discharged</td></tr></table>
<p style="color:#f85149;margin-top:12px"><strong>72.9% of N.D. Ga. Chapter 13 cases are dismissed before discharge.</strong></p>
</div></div></section>
<section><div class="container"><h2>FAQ</h2>
<details class="faq-item"><summary>How long does Chapter 7 take?</summary><div class="answer"><p>3-4 months from filing to discharge.</p></div></details>
<details class="faq-item"><summary>What if I miss a Chapter 13 payment?</summary><div class="answer"><p>Contact your attorney. You may modify the plan. Missing payments can lead to dismissal.</p></div></details>
</div></section>
<div class="container">{OBP}</div>""")

# ── CHECKLIST ──
write_page("atlanta/checklist.html",
    "Atlanta Bankruptcy Filing Checklist -- Documents Needed for N.D. Ga.",
    "Complete checklist of documents needed to file bankruptcy in Atlanta. Tax returns, pay stubs, bank statements, and everything required for N.D. Ga.",
    "https://georgiabankruptcy.org/atlanta/checklist.html",
    [("What documents do I need?","6 months pay stubs, 2 years tax returns, 3 months bank statements, all debt statements, asset list, photo ID, SSN proof, and credit counseling certificate."),
     ("What should I NOT do before filing?","Do not transfer property, pay back family, take on new debt, cash out retirement, or hide assets.")],
    bc_atl("Checklist","checklist.html"), ATL_NAV,
    f"""<div class="hero"><div class="container">
<h1>Atlanta Bankruptcy Filing Checklist</h1>
<p class="subtitle">Everything you need to gather before filing in N.D. Ga.</p>
</div></div>
<section><div class="container"><h2>Documents to Gather</h2><div class="card">
<h3>Income</h3><ul><li>Pay stubs (last 6 months)</li><li>Tax returns (last 2 years)</li><li>W-2s or 1099s (last 2 years)</li><li>Other income proof (rental, SS, pension)</li><li>P&L statement (if self-employed)</li></ul>
<h3 style="margin-top:20px">Assets</h3><ul><li>Bank statements (all accounts, 3 months)</li><li>Vehicle titles/registration</li><li>Real estate deeds + mortgage statements</li><li>Retirement account statements</li><li>Life insurance policies</li><li>Investment statements</li></ul>
<h3 style="margin-top:20px">Debts</h3><ul><li>Credit card statements</li><li>Medical bills and collection notices</li><li>Mortgage and auto loan statements</li><li>Student loan statements</li><li>Tax notices (IRS or GA DOR)</li><li>Judgments, garnishments, liens</li></ul>
<h3 style="margin-top:20px">Other</h3><ul><li>Government photo ID</li><li>Social Security card or SSN proof</li><li>Credit counseling certificate</li><li>Lawsuit documentation</li><li>Lease/rental agreement</li></ul>
</div></div></section>
<section><div class="container"><h2>Things NOT to Do Before Filing</h2><div class="card">
<ul><li><strong>Do not transfer property</strong> -- fraudulent, can deny discharge</li>
<li><strong>Do not repay family/friends</strong> -- preferential payments reversed by trustee</li>
<li><strong>Do not take on new debt</strong> -- luxury purchases within 90 days may not be dischargeable</li>
<li><strong>Do not cash out retirement</strong> -- retirement is fully exempt; cash is not</li>
<li><strong>Do not hide assets</strong> -- federal crime</li></ul>
</div></div></section>
<section><div class="container"><h2>FAQ</h2>
<details class="faq-item"><summary>How long to prepare?</summary><div class="answer"><p>1-2 weeks to gather documents. Attorney needs another 1-2 weeks for the petition.</p></div></details>
</div></section>
<div class="container">{OBP}</div>""")

# ── CREDIT AFTER BANKRUPTCY ──
write_page("atlanta/credit-after-bankruptcy.html",
    "Rebuilding Credit After Bankruptcy in Atlanta -- Practical Guide",
    "How to rebuild credit after bankruptcy in Atlanta. Timeline, secured cards, credit-builder loans, and when you can buy a house or car again.",
    "https://georgiabankruptcy.org/atlanta/credit-after-bankruptcy.html",
    [("How long does bankruptcy stay on credit?","Chapter 7: 10 years. Chapter 13: 7 years. Impact diminishes over time; most see improvement within 1-2 years."),
     ("Can I buy a house after bankruptcy?","Yes. FHA loans available 2 years after Ch. 7 discharge. Conventional loans: 4 years. VA: 2 years.")],
    bc_atl("Credit After Bankruptcy","credit-after-bankruptcy.html"), ATL_NAV,
    f"""<div class="hero"><div class="container">
<h1>Rebuilding Credit After Bankruptcy in Atlanta</h1>
<p class="subtitle">Bankruptcy is not the end -- it is a new beginning. Here is how to rebuild your credit after discharge.</p>
</div></div>
<section><div class="container"><h2>Duration on Credit Report</h2><div class="card">
<table><tr><th>Chapter</th><th>Duration</th></tr>
<tr><td>Chapter 7</td><td>10 years from filing</td></tr>
<tr><td>Chapter 13</td><td>7 years from filing</td></tr></table>
<p style="margin-top:12px">Impact diminishes significantly after 1-2 years of active rebuilding.</p>
</div></div></section>
<section><div class="container"><h2>Step-by-Step Plan</h2><div class="card">
<ol><li><strong>Check credit reports</strong> -- Verify discharged debts show $0. Dispute errors.</li>
<li><strong>Get a secured credit card</strong> -- $200-500 deposit. Use for small purchases, pay in full monthly.</li>
<li><strong>Credit-builder loan</strong> -- Some credit unions offer these.</li>
<li><strong>Pay all bills on time</strong> -- 35% of your score.</li>
<li><strong>Keep utilization under 30%</strong> -- Ideally under 10%.</li>
<li><strong>Space applications</strong> -- At least 6 months apart.</li>
<li><strong>Authorized user</strong> -- Family member's card with good history can boost your score.</li></ol>
</div></div></section>
<section><div class="container"><h2>Timeline</h2><div class="card">
<table><tr><th>When</th><th>What to Expect</th></tr>
<tr><td>Discharge day</td><td>Score may increase as debt-to-income drops</td></tr>
<tr><td>6 months</td><td>Secured card building history</td></tr>
<tr><td>1 year</td><td>May qualify for unsecured cards</td></tr>
<tr><td>2 years</td><td>Auto loans at reasonable rates; FHA mortgage eligible</td></tr>
<tr><td>3-4 years</td><td>650-700+ scores common</td></tr>
<tr><td>4 years</td><td>Conventional mortgage eligible</td></tr></table>
</div></div></section>
<section><div class="container"><h2>FAQ</h2>
<details class="faq-item"><summary>Can I buy a house?</summary><div class="answer"><p>FHA: 2 years after Ch. 7. Conventional: 4 years. VA: 2 years. <a href="https://buyahouseafterbankruptcy.com">Full guide</a>.</p></div></details>
<details class="faq-item"><summary>Can I buy a car?</summary><div class="answer"><p>Often immediately after discharge. Higher rates initially. <a href="https://buyacarafterbankruptcy.com">Guide</a>.</p></div></details>
</div></section>
<div class="container">{OBP}</div>""")

print("\n=== All 9 remaining Atlanta pages done ===\n")

# ══════════════════════════════════════════════════════════════
# SUBURBS (10 pages)
# ══════════════════════════════════════════════════════════════
suburbs = [
    ("Marietta", "marietta", "Cobb County", "northwest of Atlanta"),
    ("Roswell", "roswell", "Fulton County", "north of Atlanta"),
    ("Alpharetta", "alpharetta", "Fulton County", "north of Atlanta along GA-400"),
    ("Sandy Springs", "sandy-springs", "Fulton County", "just north of Atlanta inside the Perimeter"),
    ("Decatur", "decatur", "DeKalb County", "east of Atlanta"),
    ("Smyrna", "smyrna", "Cobb County", "northwest of Atlanta near Marietta"),
    ("Kennesaw", "kennesaw", "Cobb County", "northwest of Atlanta"),
    ("Lawrenceville", "lawrenceville", "Gwinnett County", "northeast of Atlanta"),
    ("Duluth", "duluth-ga", "Gwinnett County", "northeast of Atlanta"),
    ("Stone Mountain", "stone-mountain", "DeKalb County", "east of Atlanta"),
]

for name, slug, county, direction in suburbs:
    dn = "Duluth, GA" if slug == "duluth-ga" else name
    other_links = ''.join(f'<a href="/atlanta/suburbs/{s[1]}.html">{s[0]}</a>' for s in suburbs if s[1] != slug)

    write_page(f"atlanta/suburbs/{slug}.html",
        f"Filing Bankruptcy in {dn} -- {county} Guide | Georgia Bankruptcy",
        f"Free bankruptcy guide for {dn} residents ({county}). Filed at N.D. Ga. in Atlanta. Georgia exemptions: $21,500 homestead, $5,000 vehicle. 72.9% Ch. 13 dismissal rate.",
        f"https://georgiabankruptcy.org/atlanta/suburbs/{slug}.html",
        [(f"Where do {dn} residents file bankruptcy?",f"{dn} is in {county}, part of the Northern District of Georgia. File at 75 Ted Turner Dr SW, Atlanta, GA 30303."),
         (f"How much does bankruptcy cost in {dn}?","Filing fees: $338 Ch.7, $313 Ch.13. Attorney fees: $1,200-$2,500 for Chapter 7, $3,500-$5,000 for Chapter 13."),
         (f"What exemptions apply in {dn}?","Georgia state exemptions: $21,500 homestead, $5,000 vehicle, $600 plus $5,000 wildcard. Federal exemptions not available.")],
        [("Georgia","https://georgiabankruptcy.org"),("Atlanta","https://georgiabankruptcy.org/atlanta/"),(dn,f"https://georgiabankruptcy.org/atlanta/suburbs/{slug}.html")],
        ATL_NAV,
        f"""<div class="hero"><div class="container">
<h1>Filing Bankruptcy in {dn}</h1>
<p class="subtitle">{dn} is in {county}, {direction}. Residents file in the Northern District of Georgia, which has a 72.9% Chapter 13 dismissal rate.</p>
</div></div>
<div class="container"><div class="stats-row">
<div class="stat-card danger"><div class="number">72.9%</div><div class="label">Ch. 13 Dismissal Rate</div></div>
<div class="stat-card"><div class="number">$21,500</div><div class="label">Homestead Exemption</div></div>
<div class="stat-card"><div class="number">$5,000</div><div class="label">Vehicle Exemption</div></div>
<div class="stat-card"><div class="number">$338</div><div class="label">Ch. 7 Filing Fee</div></div>
</div></div>

<section><div class="container"><h2>Where {dn} Residents File</h2><div class="card">
<p>{dn} is in <strong>{county}</strong>, part of the <strong>Northern District of Georgia</strong>.</p>
<p><strong>U.S. Bankruptcy Court, N.D. Ga.</strong><br>75 Ted Turner Dr SW, Atlanta, GA 30303<br>Phone: (404) 215-1000 | <a href="https://www.ganb.uscourts.gov" target="_blank" rel="noopener">ganb.uscourts.gov</a></p>
</div></div></section>

<section><div class="container"><h2>Chapter 7 vs. Chapter 13</h2><div class="card">
<h3>Chapter 7 -- Fresh Start (3-4 months)</h3>
<p>Eliminates most unsecured debts. Must pass <a href="/atlanta/means-test.html">means test</a>. Fee: $338. <a href="/atlanta/chapter-7.html">Full guide &rarr;</a></p>
<h3 style="margin-top:16px">Chapter 13 -- Payment Plan (3-5 years)</h3>
<p>Keep property, catch up on mortgage. Fee: $313. <strong>72.9% dismissal rate in N.D. Ga.</strong> <a href="/atlanta/chapter-13.html">Full guide &rarr;</a></p>
</div></div></section>

<section><div class="container"><h2>Georgia Exemptions</h2><div class="card">
<table><tr><th>Property</th><th>Exemption</th></tr>
<tr><td>Homestead</td><td>$21,500 ($43,000 joint)</td></tr>
<tr><td>Vehicle</td><td>$5,000</td></tr>
<tr><td>Wildcard</td><td>$600 + up to $5,000 unused homestead</td></tr>
<tr><td>Retirement</td><td>Fully exempt</td></tr></table>
<p style="margin-top:8px"><a href="/atlanta/exemptions.html">Full exemptions &rarr;</a></p>
</div></div></section>

<section><div class="container"><h2>Cost</h2><div class="card">
<table><tr><th>Expense</th><th>Ch. 7</th><th>Ch. 13</th></tr>
<tr><td>Filing fee</td><td>$338</td><td>$313</td></tr>
<tr><td>Attorney</td><td>$1,200-$2,500</td><td>$3,500-$5,000</td></tr>
<tr><td>Counseling</td><td>$25-$50</td><td>$25-$50</td></tr></table>
<p style="margin-top:8px"><a href="/atlanta/cost.html">Full cost breakdown &rarr;</a></p>
</div></div></section>

<section><div class="container"><h2>Non-Judicial Foreclosure</h2><div class="card">
<p>Georgia allows foreclosure in as few as <strong>60 days</strong> without court. Filing bankruptcy triggers the <a href="https://automaticstay.org">automatic stay</a>, stopping it immediately. <a href="/atlanta/keep-your-house.html">Keep your house &rarr;</a></p>
</div></div></section>

<section><div class="container"><h2>Free Legal Help</h2><div class="card">
<ul><li><strong>Atlanta Legal Aid Society</strong> -- Serves {county} residents</li>
<li><strong>Atlanta Volunteer Lawyers Foundation</strong></li>
<li><strong>Georgia Legal Services Program</strong></li></ul>
</div></div></section>

<section><div class="container"><h2>FAQ</h2>
<details class="faq-item"><summary>Where do {dn} residents file?</summary><div class="answer"><p>{county}, N.D. Ga. -- 75 Ted Turner Dr SW, Atlanta, GA 30303. (404) 215-1000.</p></div></details>
<details class="faq-item"><summary>How much does it cost?</summary><div class="answer"><p>Ch. 7: $338 + $1,200-$2,500 attorney. Ch. 13: $313 + $3,500-$5,000. <a href="/atlanta/cost.html">Details</a>.</p></div></details>
<details class="faq-item"><summary>What exemptions apply?</summary><div class="answer"><p>$21,500 homestead, $5,000 vehicle, $600+$5,000 wildcard. <a href="/atlanta/exemptions.html">Full guide</a>.</p></div></details>
</div></section>

<div class="container">
<div class="card"><h3>More Atlanta Suburb Guides</h3><div class="network-links" style="margin-top:8px">{other_links}</div></div>
{OBP}
</div>""")

print("=== All 10 suburb pages done ===\n")

# ══════════════════════════════════════════════════════════════
# SAVANNAH (5 pages)
# ══════════════════════════════════════════════════════════════
SAV_NAV = '<nav><div class="container"><a href="/savannah/" class="brand">Savannah Bankruptcy Guide</a><div class="links"><a href="/">Georgia</a><a href="/savannah/">Savannah</a><a href="/savannah/chapter-7.html">Ch. 7</a><a href="/savannah/chapter-13.html">Ch. 13</a><a href="/savannah/exemptions.html">Exemptions</a><a href="/savannah/faq.html">FAQ</a></div></div></nav>'
bc_sav = lambda n,u: [("Georgia","https://georgiabankruptcy.org"),("Savannah","https://georgiabankruptcy.org/savannah/"),(n,f"https://georgiabankruptcy.org/savannah/{u}")]

# Savannah Index
write_page("savannah/index.html",
    "Filing Bankruptcy in Savannah, Georgia -- S.D. Ga. Guide",
    "Free 2026 guide to filing bankruptcy in Savannah. S.D. Ga. courthouse at 125 Bull St. Georgia exemptions, Chapter 7, Chapter 13, and costs.",
    "https://georgiabankruptcy.org/savannah/",
    [("Where do I file in Savannah?","Southern District of Georgia, 125 Bull St, Savannah, GA 31401. Phone: (912) 650-4100."),
     ("How much does it cost?","Filing: $338 Ch.7, $313 Ch.13. Attorney: $1,000-$2,000 Ch.7, $3,000-$4,500 Ch.13.")],
    [("Georgia","https://georgiabankruptcy.org"),("Savannah","https://georgiabankruptcy.org/savannah/")],
    SAV_NAV,
    f"""<div class="hero"><div class="container">
<h1>Filing Bankruptcy in Savannah, Georgia</h1>
<p class="subtitle">Savannah is served by the Southern District of Georgia. This free guide covers everything Savannah-area residents need to know.</p>
</div></div>
<div class="container"><div class="stats-row">
<div class="stat-card"><div class="number">$21,500</div><div class="label">Homestead Exemption</div></div>
<div class="stat-card"><div class="number">$5,000</div><div class="label">Vehicle Exemption</div></div>
<div class="stat-card"><div class="number">$338</div><div class="label">Ch. 7 Filing Fee</div></div>
<div class="stat-card"><div class="number">$313</div><div class="label">Ch. 13 Filing Fee</div></div>
</div></div>
<section><div class="container"><h2>S.D. Ga. Courthouse</h2><div class="card">
<p><strong>U.S. Bankruptcy Court, S.D. Ga.</strong><br>125 Bull St, Savannah, GA 31401<br>Phone: (912) 650-4100 | <a href="https://www.gasb.uscourts.gov" target="_blank" rel="noopener">gasb.uscourts.gov</a></p>
<p>Covers southeastern Georgia including Savannah, Brunswick, and Statesboro.</p>
</div></div></section>
<section><div class="container"><h2>Chapter 7 vs. Chapter 13</h2><div class="card">
<h3>Chapter 7 (3-4 months)</h3><p>Eliminates unsecured debts. <a href="/savannah/chapter-7.html">Full guide &rarr;</a></p>
<h3 style="margin-top:16px">Chapter 13 (3-5 years)</h3><p>Repayment plan, keep property. <a href="/savannah/chapter-13.html">Full guide &rarr;</a></p>
</div></div></section>
<section><div class="container"><h2>Georgia Exemptions</h2><div class="card">
<table><tr><th>Property</th><th>Exemption</th></tr>
<tr><td>Homestead</td><td>$21,500 ($43,000 joint)</td></tr>
<tr><td>Vehicle</td><td>$5,000</td></tr>
<tr><td>Wildcard</td><td>$600 + up to $5,000 unused homestead</td></tr>
<tr><td>Retirement</td><td>Fully exempt</td></tr></table>
<p><a href="/savannah/exemptions.html">Full guide &rarr;</a></p>
</div></div></section>
<section><div class="container"><h2>Foreclosure Warning</h2><div class="card">
<p>Georgia is non-judicial foreclosure -- as fast as 60 days. <a href="https://automaticstay.org">Automatic stay</a> stops it immediately.</p>
</div></div></section>
<section><div class="container"><h2>Free Legal Help</h2><div class="card">
<ul><li><strong>Georgia Legal Services Program</strong></li><li><strong>Savannah Bar Association Lawyer Referral</strong></li></ul>
</div></div></section>
<section><div class="container"><h2>FAQ</h2>
<details class="faq-item"><summary>Where do I file?</summary><div class="answer"><p>125 Bull St, Savannah, GA 31401. (912) 650-4100.</p></div></details>
<details class="faq-item"><summary>How much does it cost?</summary><div class="answer"><p>Ch. 7: $338 + $1,000-$2,000 attorney. Ch. 13: $313 + $3,000-$4,500.</p></div></details>
</div></section>
<div class="container"><div class="card"><h3>Other Georgia Cities</h3><div class="network-links"><a href="/atlanta/">Atlanta</a><a href="/macon/">Macon</a></div></div>{OBP}</div>""")

# Savannah Ch7
write_page("savannah/chapter-7.html",
    "Chapter 7 Bankruptcy in Savannah, GA -- S.D. Ga. Guide",
    "Chapter 7 guide for Savannah. Means test, Georgia exemptions, S.D. Ga. courthouse, timeline, and debts eliminated.",
    "https://georgiabankruptcy.org/savannah/chapter-7.html",
    [("Do I qualify for Chapter 7 in Savannah?","Below Georgia median income (~$55,000 single) = automatic qualification. Above = may qualify after expense deductions."),
     ("How long does Chapter 7 take?","3-4 months from filing to discharge in S.D. Ga.")],
    bc_sav("Chapter 7","chapter-7.html"), SAV_NAV,
    f"""<div class="hero"><div class="container"><h1>Chapter 7 Bankruptcy in Savannah</h1>
<p class="subtitle">Eliminates most unsecured debts in 3-4 months. Filed at S.D. Ga., 125 Bull St.</p></div></div>
<section><div class="container"><h2>Means Test</h2><div class="card">
<table><tr><th>Household</th><th>Median</th></tr><tr><td>1</td><td>$55,000</td></tr><tr><td>2</td><td>$70,000</td></tr><tr><td>3</td><td>$78,000</td></tr><tr><td>4</td><td>$91,000</td></tr></table>
</div></div></section>
<section><div class="container"><h2>Debts Eliminated</h2><div class="card">
<ul><li>Credit cards, medical bills, personal loans, utility arrears, deficiency balances</li></ul>
<p><strong>Not eliminated:</strong> Student loans, recent taxes, child support, alimony.</p>
</div></div></section>
<section><div class="container"><h2>Exemptions</h2><div class="card">
<table><tr><th>Property</th><th>Amount</th></tr><tr><td>Homestead</td><td>$21,500</td></tr><tr><td>Vehicle</td><td>$5,000</td></tr><tr><td>Wildcard</td><td>$600+$5,000</td></tr><tr><td>Retirement</td><td>Fully exempt</td></tr></table>
<p><a href="/savannah/exemptions.html">Full guide &rarr;</a></p>
</div></div></section>
<section><div class="container"><h2>Timeline</h2><div class="card">
<ol><li>Credit counseling (before filing)</li><li>File petition -- stay begins</li><li>341 meeting (~30 days)</li><li>Debtor education</li><li>Discharge (~90-120 days)</li></ol>
</div></div></section>
<section><div class="container"><h2>FAQ</h2>
<details class="faq-item"><summary>Do I qualify?</summary><div class="answer"><p>Below median = yes. Above = may qualify after deductions.</p></div></details>
<details class="faq-item"><summary>How long?</summary><div class="answer"><p>3-4 months.</p></div></details>
</div></section>
<div class="container">{OBP}</div>""")

# Savannah Ch13
write_page("savannah/chapter-13.html",
    "Chapter 13 Bankruptcy in Savannah, GA -- Repayment Plan Guide",
    "Chapter 13 guide for Savannah. Repayment plans, stopping foreclosure, S.D. Ga. procedures, keeping property.",
    "https://georgiabankruptcy.org/savannah/chapter-13.html",
    [("How does Chapter 13 work in Savannah?","3-5 year repayment plan. Keep property, stop foreclosure. Filed at 125 Bull St."),
     ("Can it stop foreclosure?","Yes. Automatic stay halts it immediately. Catch up on arrears through the plan.")],
    bc_sav("Chapter 13","chapter-13.html"), SAV_NAV,
    f"""<div class="hero"><div class="container"><h1>Chapter 13 Bankruptcy in Savannah</h1>
<p class="subtitle">Keep your property while repaying debts over 3-5 years through a court-supervised plan.</p></div></div>
<section><div class="container"><h2>How It Works</h2><div class="card">
<ul><li>Keep all property</li><li>Stop foreclosure, catch up on mortgage</li><li>Protect co-signers</li><li>Pay taxes over time</li><li>No means test</li></ul>
<p>Filed at 125 Bull St, Savannah, GA 31401. Fee: $313.</p>
</div></div></section>
<section><div class="container"><h2>Stopping Foreclosure</h2><div class="card">
<p>Georgia: non-judicial foreclosure in 60 days. Chapter 13 is your defense:</p>
<ol><li><a href="https://automaticstay.org">Automatic stay</a> stops foreclosure</li><li>Resume regular payments</li><li>Arrears paid through 3-5 year plan</li></ol>
</div></div></section>
<section><div class="container"><h2>Plan Duration</h2><div class="card">
<p>Below median: 3 years. Above: 5 years. Attorney fees ($3,000-$4,500) usually paid through plan.</p>
</div></div></section>
<section><div class="container"><h2>FAQ</h2>
<details class="faq-item"><summary>How does it work?</summary><div class="answer"><p>3-5 year plan, monthly payments to trustee, keep all property.</p></div></details>
<details class="faq-item"><summary>Stop foreclosure?</summary><div class="answer"><p>Yes, immediately via automatic stay.</p></div></details>
</div></section>
<div class="container">{OBP}</div>""")

# Savannah Exemptions
write_page("savannah/exemptions.html",
    "Georgia Exemptions for Savannah Bankruptcy Filers -- 2026",
    "Georgia bankruptcy exemptions for Savannah. Homestead $21,500, vehicle $5,000, wildcard $600+$5,000. S.D. Ga. guide.",
    "https://georgiabankruptcy.org/savannah/exemptions.html",
    [("What is Georgia homestead exemption?","$21,500 ($43,000 joint). Federal exemptions not available."),
     ("Is retirement protected?","Yes. 401(k), IRA, pension fully exempt, no limit.")],
    bc_sav("Exemptions","exemptions.html"), SAV_NAV,
    f"""<div class="hero"><div class="container"><h1>Georgia Exemptions for Savannah Filers</h1>
<p class="subtitle">Georgia requires state exemptions only. Here is what you can protect.</p></div></div>
<section><div class="container"><h2>Exemption Table</h2><div class="card">
<table><tr><th>Property</th><th>Amount</th></tr>
<tr><td>Homestead</td><td>$21,500 ($43,000 joint)</td></tr>
<tr><td>Vehicle</td><td>$5,000</td></tr>
<tr><td>Household goods</td><td>$600/item, $5,000 total</td></tr>
<tr><td>Jewelry</td><td>$500</td></tr>
<tr><td>Wildcard</td><td>$600 + up to $5,000 unused homestead</td></tr>
<tr><td>Tools of trade</td><td>$1,500</td></tr>
<tr><td>Retirement</td><td>Fully exempt</td></tr>
<tr><td>Social Security</td><td>Fully exempt</td></tr>
<tr><td>Workers comp</td><td>Fully exempt</td></tr>
<tr><td>Life insurance</td><td>Fully exempt</td></tr>
<tr><td>Personal injury</td><td>$10,000</td></tr></table>
</div></div></section>
<section><div class="container"><h2>FAQ</h2>
<details class="faq-item"><summary>Can I use federal exemptions?</summary><div class="answer"><p>No. Georgia opted out.</p></div></details>
<details class="faq-item"><summary>Is retirement protected?</summary><div class="answer"><p>Yes. Fully exempt, no limit.</p></div></details>
</div></section>
<div class="container">{OBP}</div>""")

# Savannah FAQ
write_page("savannah/faq.html",
    "Savannah Bankruptcy FAQ -- S.D. Ga. Common Questions",
    "FAQ for filing bankruptcy in Savannah. S.D. Ga. courthouse, exemptions, costs, procedures.",
    "https://georgiabankruptcy.org/savannah/faq.html",
    [("Where do I file?","125 Bull St, Savannah, GA 31401. (912) 650-4100."),
     ("How much does it cost?","Ch. 7: $338+$1,000-$2,000. Ch. 13: $313+$3,000-$4,500.")],
    bc_sav("FAQ","faq.html"), SAV_NAV,
    f"""<div class="hero"><div class="container"><h1>Savannah Bankruptcy FAQ</h1>
<p class="subtitle">Common questions about filing in the Southern District of Georgia.</p></div></div>
<section><div class="container"><h2>Filing</h2>
<details class="faq-item"><summary>Where do I file?</summary><div class="answer"><p>125 Bull St, Savannah, GA 31401. (912) 650-4100. <a href="https://www.gasb.uscourts.gov">gasb.uscourts.gov</a>.</p></div></details>
<details class="faq-item"><summary>Chapter 7 or 13?</summary><div class="answer"><p>Ch. 7: fast fresh start. Ch. 13: keep property, stop foreclosure. <a href="https://chapter7vs13.org">Compare</a>.</p></div></details>
</div></section>
<section><div class="container"><h2>Costs</h2>
<details class="faq-item"><summary>How much?</summary><div class="answer"><p>Ch. 7: $338+$1,000-$2,000 attorney. Ch. 13: $313+$3,000-$4,500 (through plan).</p></div></details>
</div></section>
<section><div class="container"><h2>Property</h2>
<details class="faq-item"><summary>Will I lose my house?</summary><div class="answer"><p>Under $21,500 equity: keep it. Ch. 13: catch up on payments. <a href="/savannah/exemptions.html">Exemptions</a>.</p></div></details>
<details class="faq-item"><summary>Will I lose my car?</summary><div class="answer"><p>$5,000 exemption + wildcard protects most cars.</p></div></details>
<details class="faq-item"><summary>Retirement protected?</summary><div class="answer"><p>Yes, fully exempt.</p></div></details>
</div></section>
<section><div class="container"><h2>Foreclosure</h2>
<details class="faq-item"><summary>Stop foreclosure?</summary><div class="answer"><p>Yes. <a href="https://automaticstay.org">Automatic stay</a> halts it. Georgia: non-judicial, 60 days.</p></div></details>
<details class="faq-item"><summary>Stop garnishment?</summary><div class="answer"><p>Yes, immediately upon filing.</p></div></details>
</div></section>
<section><div class="container"><h2>After Bankruptcy</h2>
<details class="faq-item"><summary>How long on credit?</summary><div class="answer"><p>Ch. 7: 10 years. Ch. 13: 7 years. Improvement in 1-2 years.</p></div></details>
<details class="faq-item"><summary>File again?</summary><div class="answer"><p>Yes, with waiting periods. <a href="https://filebankruptcyagain.com">Guide</a>.</p></div></details>
</div></section>
<div class="container">{OBP}</div>""")

print("=== All 5 Savannah pages done ===\n")

# ══════════════════════════════════════════════════════════════
# MACON (5 pages)
# ══════════════════════════════════════════════════════════════
MAC_NAV = '<nav><div class="container"><a href="/macon/" class="brand">Macon Bankruptcy Guide</a><div class="links"><a href="/">Georgia</a><a href="/macon/">Macon</a><a href="/macon/chapter-7.html">Ch. 7</a><a href="/macon/chapter-13.html">Ch. 13</a><a href="/macon/exemptions.html">Exemptions</a><a href="/macon/faq.html">FAQ</a></div></div></nav>'
bc_mac = lambda n,u: [("Georgia","https://georgiabankruptcy.org"),("Macon","https://georgiabankruptcy.org/macon/"),(n,f"https://georgiabankruptcy.org/macon/{u}")]

# Macon Index
write_page("macon/index.html",
    "Filing Bankruptcy in Macon, Georgia -- M.D. Ga. Guide",
    "Free 2026 guide to filing bankruptcy in Macon. M.D. Ga. courthouse at 475 Mulberry St. Georgia exemptions, Chapter 7, Chapter 13, costs.",
    "https://georgiabankruptcy.org/macon/",
    [("Where do I file in Macon?","Middle District of Georgia, 475 Mulberry St, Macon, GA 31201. (478) 752-3506."),
     ("How much does it cost?","Ch. 7: $338+$1,000-$1,800. Ch. 13: $313+$2,500-$4,000.")],
    [("Georgia","https://georgiabankruptcy.org"),("Macon","https://georgiabankruptcy.org/macon/")],
    MAC_NAV,
    f"""<div class="hero"><div class="container"><h1>Filing Bankruptcy in Macon, Georgia</h1>
<p class="subtitle">Macon is served by the Middle District of Georgia. This free guide covers everything Macon-area residents need to know.</p></div></div>
<div class="container"><div class="stats-row">
<div class="stat-card"><div class="number">$21,500</div><div class="label">Homestead Exemption</div></div>
<div class="stat-card"><div class="number">$5,000</div><div class="label">Vehicle Exemption</div></div>
<div class="stat-card"><div class="number">$338</div><div class="label">Ch. 7 Filing Fee</div></div>
<div class="stat-card"><div class="number">$313</div><div class="label">Ch. 13 Filing Fee</div></div>
</div></div>
<section><div class="container"><h2>M.D. Ga. Courthouse</h2><div class="card">
<p><strong>U.S. Bankruptcy Court, M.D. Ga.</strong><br>475 Mulberry St, Macon, GA 31201<br>Phone: (478) 752-3506 | <a href="https://www.gamb.uscourts.gov" target="_blank" rel="noopener">gamb.uscourts.gov</a></p>
<p>Covers central Georgia: Macon, Albany, Columbus, Valdosta, and surrounding areas.</p>
</div></div></section>
<section><div class="container"><h2>Chapter 7 vs. Chapter 13</h2><div class="card">
<h3>Chapter 7 (3-4 months)</h3><p>Eliminates unsecured debts. <a href="/macon/chapter-7.html">Guide &rarr;</a></p>
<h3 style="margin-top:16px">Chapter 13 (3-5 years)</h3><p>Repayment plan, keep property. <a href="/macon/chapter-13.html">Guide &rarr;</a></p>
</div></div></section>
<section><div class="container"><h2>Exemptions</h2><div class="card">
<table><tr><th>Property</th><th>Exemption</th></tr>
<tr><td>Homestead</td><td>$21,500 ($43,000 joint)</td></tr>
<tr><td>Vehicle</td><td>$5,000</td></tr>
<tr><td>Wildcard</td><td>$600 + up to $5,000</td></tr>
<tr><td>Retirement</td><td>Fully exempt</td></tr></table>
<p><a href="/macon/exemptions.html">Full guide &rarr;</a></p>
</div></div></section>
<section><div class="container"><h2>Foreclosure</h2><div class="card">
<p>Georgia: non-judicial, 60 days. <a href="https://automaticstay.org">Automatic stay</a> stops it.</p>
</div></div></section>
<section><div class="container"><h2>Free Legal Help</h2><div class="card">
<ul><li><strong>Georgia Legal Services Program</strong></li><li><strong>Macon Bar Association</strong></li></ul>
</div></div></section>
<section><div class="container"><h2>FAQ</h2>
<details class="faq-item"><summary>Where do I file?</summary><div class="answer"><p>475 Mulberry St, Macon, GA 31201. (478) 752-3506.</p></div></details>
<details class="faq-item"><summary>How much?</summary><div class="answer"><p>Ch. 7: $338+$1,000-$1,800. Ch. 13: $313+$2,500-$4,000.</p></div></details>
</div></section>
<div class="container"><div class="card"><h3>Other Georgia Cities</h3><div class="network-links"><a href="/atlanta/">Atlanta</a><a href="/savannah/">Savannah</a></div></div>{OBP}</div>""")

# Macon Ch7
write_page("macon/chapter-7.html",
    "Chapter 7 Bankruptcy in Macon, GA -- M.D. Ga. Guide",
    "Chapter 7 guide for Macon. Means test, Georgia exemptions, M.D. Ga. courthouse at 475 Mulberry St, timeline.",
    "https://georgiabankruptcy.org/macon/chapter-7.html",
    [("Do I qualify in Macon?","Below Georgia median (~$55,000 single) = yes. Above = may qualify after deductions."),
     ("How long?","3-4 months from filing to discharge.")],
    bc_mac("Chapter 7","chapter-7.html"), MAC_NAV,
    f"""<div class="hero"><div class="container"><h1>Chapter 7 Bankruptcy in Macon</h1>
<p class="subtitle">Eliminates most unsecured debts in 3-4 months. Filed at M.D. Ga., 475 Mulberry St.</p></div></div>
<section><div class="container"><h2>Means Test</h2><div class="card">
<table><tr><th>Household</th><th>Median</th></tr><tr><td>1</td><td>$55,000</td></tr><tr><td>2</td><td>$70,000</td></tr><tr><td>3</td><td>$78,000</td></tr><tr><td>4</td><td>$91,000</td></tr></table>
</div></div></section>
<section><div class="container"><h2>Debts Eliminated</h2><div class="card">
<ul><li>Credit cards, medical bills, personal loans, utility arrears</li></ul>
<p><strong>Not:</strong> Student loans, recent taxes, support obligations.</p>
</div></div></section>
<section><div class="container"><h2>Exemptions</h2><div class="card">
<table><tr><th>Property</th><th>Amount</th></tr><tr><td>Homestead</td><td>$21,500</td></tr><tr><td>Vehicle</td><td>$5,000</td></tr><tr><td>Wildcard</td><td>$600+$5,000</td></tr><tr><td>Retirement</td><td>Fully exempt</td></tr></table>
</div></div></section>
<section><div class="container"><h2>Timeline</h2><div class="card">
<ol><li>Credit counseling</li><li>File petition (stay begins)</li><li>341 meeting (~30 days)</li><li>Debtor education</li><li>Discharge (~90-120 days)</li></ol>
</div></div></section>
<section><div class="container"><h2>FAQ</h2>
<details class="faq-item"><summary>Qualify?</summary><div class="answer"><p>Below median = yes. Above = maybe after deductions.</p></div></details>
</div></section>
<div class="container">{OBP}</div>""")

# Macon Ch13
write_page("macon/chapter-13.html",
    "Chapter 13 Bankruptcy in Macon, GA -- Repayment Plan Guide",
    "Chapter 13 guide for Macon. Repayment plans, stopping foreclosure, M.D. Ga. procedures.",
    "https://georgiabankruptcy.org/macon/chapter-13.html",
    [("How does Chapter 13 work in Macon?","3-5 year plan, keep property, stop foreclosure. Filed at 475 Mulberry St."),
     ("Stop foreclosure?","Yes. Automatic stay halts it. Arrears paid through plan.")],
    bc_mac("Chapter 13","chapter-13.html"), MAC_NAV,
    f"""<div class="hero"><div class="container"><h1>Chapter 13 Bankruptcy in Macon</h1>
<p class="subtitle">Reorganize debts over 3-5 years while keeping property and stopping foreclosure.</p></div></div>
<section><div class="container"><h2>How It Works</h2><div class="card">
<ul><li>Keep all property</li><li>Stop foreclosure</li><li>Protect co-signers</li><li>No means test</li></ul>
<p>Filed at 475 Mulberry St, Macon, GA 31201. Fee: $313.</p>
</div></div></section>
<section><div class="container"><h2>Stopping Foreclosure</h2><div class="card">
<p>Georgia: non-judicial, 60 days. Automatic stay stops it. Arrears spread over 3-5 years.</p>
</div></div></section>
<section><div class="container"><h2>Plan Duration</h2><div class="card">
<p>Below median: 3 years. Above: 5 years. Attorney fees ($2,500-$4,000) usually through plan.</p>
</div></div></section>
<section><div class="container"><h2>FAQ</h2>
<details class="faq-item"><summary>How does it work?</summary><div class="answer"><p>Monthly payments to trustee for 3-5 years. Keep all property.</p></div></details>
</div></section>
<div class="container">{OBP}</div>""")

# Macon Exemptions
write_page("macon/exemptions.html",
    "Georgia Exemptions for Macon Bankruptcy Filers -- 2026",
    "Georgia bankruptcy exemptions for Macon. Homestead $21,500, vehicle $5,000, wildcard $600+$5,000. M.D. Ga. guide.",
    "https://georgiabankruptcy.org/macon/exemptions.html",
    [("What exemptions apply?","Georgia state: $21,500 homestead, $5,000 vehicle, $600+$5,000 wildcard. No federal."),
     ("Retirement protected?","Yes. Fully exempt, no limit.")],
    bc_mac("Exemptions","exemptions.html"), MAC_NAV,
    f"""<div class="hero"><div class="container"><h1>Georgia Exemptions for Macon Filers</h1>
<p class="subtitle">State exemptions only -- no federal option in Georgia.</p></div></div>
<section><div class="container"><h2>Exemption Table</h2><div class="card">
<table><tr><th>Property</th><th>Amount</th></tr>
<tr><td>Homestead</td><td>$21,500 ($43,000 joint)</td></tr>
<tr><td>Vehicle</td><td>$5,000</td></tr>
<tr><td>Household goods</td><td>$600/item, $5,000 total</td></tr>
<tr><td>Jewelry</td><td>$500</td></tr>
<tr><td>Wildcard</td><td>$600 + up to $5,000</td></tr>
<tr><td>Tools of trade</td><td>$1,500</td></tr>
<tr><td>Retirement</td><td>Fully exempt</td></tr>
<tr><td>Social Security</td><td>Fully exempt</td></tr>
<tr><td>Workers comp</td><td>Fully exempt</td></tr>
<tr><td>Life insurance</td><td>Fully exempt</td></tr>
<tr><td>Personal injury</td><td>$10,000</td></tr></table>
</div></div></section>
<section><div class="container"><h2>FAQ</h2>
<details class="faq-item"><summary>Federal exemptions?</summary><div class="answer"><p>No. Georgia opted out.</p></div></details>
<details class="faq-item"><summary>Retirement?</summary><div class="answer"><p>Fully exempt, no limit.</p></div></details>
</div></section>
<div class="container">{OBP}</div>""")

# Macon FAQ
write_page("macon/faq.html",
    "Macon Bankruptcy FAQ -- M.D. Ga. Common Questions",
    "FAQ for filing bankruptcy in Macon. M.D. Ga. courthouse, exemptions, costs, procedures.",
    "https://georgiabankruptcy.org/macon/faq.html",
    [("Where do I file?","475 Mulberry St, Macon, GA 31201. (478) 752-3506."),
     ("How much?","Ch. 7: $338+$1,000-$1,800. Ch. 13: $313+$2,500-$4,000.")],
    bc_mac("FAQ","faq.html"), MAC_NAV,
    f"""<div class="hero"><div class="container"><h1>Macon Bankruptcy FAQ</h1>
<p class="subtitle">Common questions about filing in the Middle District of Georgia.</p></div></div>
<section><div class="container"><h2>Filing</h2>
<details class="faq-item"><summary>Where do I file?</summary><div class="answer"><p>475 Mulberry St, Macon, GA 31201. (478) 752-3506. <a href="https://www.gamb.uscourts.gov">gamb.uscourts.gov</a>.</p></div></details>
<details class="faq-item"><summary>Chapter 7 or 13?</summary><div class="answer"><p>Ch. 7: quick (3-4 months), means test required. Ch. 13: 3-5 year plan, no means test. <a href="https://chapter7vs13.org">Compare</a>.</p></div></details>
</div></section>
<section><div class="container"><h2>Costs</h2>
<details class="faq-item"><summary>How much?</summary><div class="answer"><p>Ch. 7: $338+$1,000-$1,800. Ch. 13: $313+$2,500-$4,000 (through plan). Counseling: $25-$50.</p></div></details>
</div></section>
<section><div class="container"><h2>Property</h2>
<details class="faq-item"><summary>Lose my house?</summary><div class="answer"><p>Under $21,500 equity: no. Ch. 13: catch up on payments. <a href="/macon/exemptions.html">Exemptions</a>.</p></div></details>
<details class="faq-item"><summary>Lose my car?</summary><div class="answer"><p>$5,000 exemption + wildcard protects most cars.</p></div></details>
<details class="faq-item"><summary>Retirement?</summary><div class="answer"><p>Fully exempt.</p></div></details>
</div></section>
<section><div class="container"><h2>Foreclosure</h2>
<details class="faq-item"><summary>Stop foreclosure?</summary><div class="answer"><p>Yes. <a href="https://automaticstay.org">Automatic stay</a> stops it. Georgia: 60 days non-judicial.</p></div></details>
</div></section>
<section><div class="container"><h2>After</h2>
<details class="faq-item"><summary>Credit impact?</summary><div class="answer"><p>Ch. 7: 10 years. Ch. 13: 7 years. Improvement in 1-2 years.</p></div></details>
<details class="faq-item"><summary>File again?</summary><div class="answer"><p>Yes, with waiting periods. <a href="https://filebankruptcyagain.com">Guide</a>.</p></div></details>
</div></section>
<div class="container">{OBP}</div>""")

print("=== All 5 Macon pages done ===")
print("\n=== TOTAL: 29 pages generated ===")
