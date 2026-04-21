#!/usr/bin/env python3
"""Generate all missing pages for georgiabankruptcy.org"""
import pathlib

BASE = pathlib.Path(__file__).parent
GA4 = '<script async src="https://www.googletagmanager.com/gtag/js?id=G-CSBPNV4NKL"></script>\n<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag(\'js\',new Date());gtag(\'config\',\'G-CSBPNV4NKL\');gtag(\'config\',\'G-053Z64N82F\');gtag(\'config\',\'G-FTWLM223G7\');</script>'

CSS = """*{margin:0;padding:0;box-sizing:border-box}body{background:#0d1117;color:#c9d1d9;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;line-height:1.6}a{color:#58a6ff;text-decoration:none}a:hover{text-decoration:underline}.container{max-width:1100px;margin:0 auto;padding:0 20px}nav{background:#161b22;border-bottom:1px solid #30363d;padding:12px 0;position:sticky;top:0;z-index:100}nav .container{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px}nav .brand{color:#f0f6fc;font-weight:700;font-size:1.1rem}nav .links{display:flex;gap:16px;flex-wrap:wrap}nav .links a{color:#8b949e;font-size:0.9rem}nav .links a:hover{color:#58a6ff}.hero{padding:60px 0 40px;text-align:center;border-bottom:1px solid #30363d}.hero h1{color:#f0f6fc;font-size:2.4rem;margin-bottom:12px}.hero .subtitle{color:#8b949e;font-size:1.15rem;max-width:700px;margin:0 auto}section{padding:40px 0;border-bottom:1px solid #21262d}h2{color:#f0f6fc;font-size:1.8rem;margin-bottom:16px}h3{color:#f0f6fc;font-size:1.3rem;margin-bottom:12px}p{margin-bottom:16px}.card{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:24px;margin-bottom:20px}.faq-item{background:#161b22;border:1px solid #30363d;border-radius:8px;margin-bottom:12px;overflow:hidden}.faq-item summary{padding:16px 20px;cursor:pointer;color:#f0f6fc;font-weight:600;list-style:none;display:flex;justify-content:space-between;align-items:center}.faq-item summary::after{content:"+";color:#58a6ff;font-size:1.3rem;font-weight:700}.faq-item[open] summary::after{content:"-"}.faq-item .answer{padding:0 20px 16px;color:#c9d1d9}.network{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:24px;margin:32px 0}.network h3{margin-bottom:12px}.network-links{display:flex;flex-wrap:wrap;gap:8px}.network-links a{background:#21262d;padding:6px 14px;border-radius:16px;font-size:0.85rem;border:1px solid #30363d}.network-links a:hover{border-color:#58a6ff;background:#161b22}footer{background:#161b22;border-top:1px solid #30363d;padding:32px 0;text-align:center;color:#8b949e;font-size:0.85rem}footer a{color:#58a6ff}footer p{margin-bottom:8px}.cta{display:inline-block;background:#238636;color:#fff;padding:12px 28px;border-radius:6px;font-weight:600;margin-top:12px;font-size:1rem}.cta:hover{background:#2ea043;text-decoration:none}ul,ol{margin:12px 0 12px 24px}li{margin-bottom:6px}table{width:100%;border-collapse:collapse;margin:16px 0}th,td{padding:10px 14px;text-align:left;border-bottom:1px solid #30363d}th{color:#f0f6fc;background:#161b22;font-weight:600}td{color:#c9d1d9}.stats-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;padding:32px 0}.stat-card{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:24px;text-align:center}.stat-card .number{color:#58a6ff;font-size:2.2rem;font-weight:700}.stat-card .label{color:#8b949e;font-size:0.9rem;margin-top:4px}.stat-card.danger .number{color:#f85149}.district-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:16px}.district-card{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:20px}.district-card h3{margin-bottom:8px;font-size:1.15rem}.district-card .meta{color:#8b949e;font-size:0.85rem;margin-top:8px}@media(max-width:768px){.hero h1{font-size:1.7rem}.stats-row{grid-template-columns:1fr 1fr}.stat-card .number{font-size:1.6rem}}@media(max-width:480px){.stats-row{grid-template-columns:1fr}}"""

FOOTER = """<footer><div class="container">
<p>An <a href="https://openbankruptcyproject.org">Open Bankruptcy Project</a> resource</p>
<p>Data sourced from the Federal Judicial Center Integrated Database (2008--2024).</p>
<p>This site provides general information, not legal advice. Consult a qualified attorney for your specific situation.</p>
<p>&copy; 2026 Open Bankruptcy Project. <a href="https://github.com/openbankruptcyproject">GitHub</a></p>
</div></footer>
<script src="/btn-engage.js"></script>"""

OBP_NETWORK = """<div class="network">
<h3>Open Bankruptcy Project Network</h3>
<div class="network-links">
<a href="https://openbankruptcyproject.org">OBP Home</a>
<a href="https://1328f.com">1328(f) Screener</a>
<a href="https://chapter7vs13.org">Ch. 7 vs 13</a>
<a href="https://automaticstay.org">Automatic Stay</a>
<a href="https://341meeting.org">341 Meeting</a>
<a href="https://bankruptcymeanstest.org">Means Test</a>
<a href="https://howmuchdoesbankruptcycost.com">Cost Guide</a>
<a href="https://bankruptcydismissed.com">Dismissed?</a>
<a href="https://filebankruptcyagain.com">File Again?</a>
<a href="https://howtofilebankruptcy.org">How to File</a>
</div>
</div>"""

ATL_NAV = '<nav><div class="container"><a href="/atlanta/" class="brand">Atlanta Bankruptcy Guide</a><div class="links"><a href="/">Georgia</a><a href="/atlanta/">Atlanta</a><a href="/atlanta/chapter-7.html">Chapter 7</a><a href="/atlanta/chapter-13.html">Chapter 13</a><a href="/atlanta/exemptions.html">Exemptions</a><a href="/atlanta/cost.html">Cost</a><a href="/atlanta/faq.html">FAQ</a></div></div></nav>'

SAV_NAV = '<nav><div class="container"><a href="/savannah/" class="brand">Savannah Bankruptcy Guide</a><div class="links"><a href="/">Georgia</a><a href="/savannah/">Savannah</a><a href="/savannah/chapter-7.html">Chapter 7</a><a href="/savannah/chapter-13.html">Chapter 13</a><a href="/savannah/exemptions.html">Exemptions</a><a href="/savannah/faq.html">FAQ</a></div></div></nav>'

MAC_NAV = '<nav><div class="container"><a href="/macon/" class="brand">Macon Bankruptcy Guide</a><div class="links"><a href="/">Georgia</a><a href="/macon/">Macon</a><a href="/macon/chapter-7.html">Chapter 7</a><a href="/macon/chapter-13.html">Chapter 13</a><a href="/macon/exemptions.html">Exemptions</a><a href="/macon/faq.html">FAQ</a></div></div></nav>'

def faq_schema(faqs):
    items = ','.join([f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
                      for q, a in faqs])
    return f'{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{items}]}}'

def breadcrumb_schema(crumbs):
    items = ','.join([f'{{"@type":"ListItem","position":{i+1},"name":"{n}","item":"{u}"}}'
                      for i,(n,u) in enumerate(crumbs)])
    return f'{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{items}]}}'

def page(title, desc, canonical, nav, breadcrumbs, faqs, body_html):
    bc = breadcrumb_schema(breadcrumbs)
    fs = faq_schema(faqs)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="canonical" href="{canonical}">
{GA4}
<script type="application/ld+json">
{fs}
</script>
<script type="application/ld+json">
{bc}
</script>
<style>
{CSS}
</style>
</head>
<body>
{nav}

{body_html}

<div class="container">
{OBP_NETWORK}
</div>

{FOOTER}
</body>
</html>"""

def write_if_missing(rel_path, html):
    fp = BASE / rel_path
    if fp.exists():
        print(f"  SKIP (exists): {rel_path}")
        return False
    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_text(html, encoding='utf-8')
    print(f"  CREATED: {rel_path}")
    return True

created = 0

# ============================================================
# ATLANTA - 9 missing topic pages
# ============================================================

# means-test
html = page(
    "Atlanta Bankruptcy Means Test -- 2026 Guide | Georgia Bankruptcy",
    "How the bankruptcy means test works for Atlanta filers. Georgia median income thresholds, expense deductions, and how to determine Chapter 7 eligibility in the Northern District.",
    "https://georgiabankruptcy.org/atlanta/means-test.html",
    ATL_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Atlanta","https://georgiabankruptcy.org/atlanta/"),("Means Test","https://georgiabankruptcy.org/atlanta/means-test.html")],
    [("What is the means test for Atlanta bankruptcy?","The means test compares your household income to Georgia's median. For a single filer, the 2026 Georgia median is approximately $55,000. If below, you automatically qualify for Chapter 7. If above, you may still qualify after deducting allowed expenses."),
     ("What if I fail the means test?","Failing the means test does not mean you cannot file bankruptcy. You may still qualify for Chapter 7 after deducting allowed expenses, or you can file Chapter 13, which has no income limit."),
     ("What income counts for the means test?","The means test uses your average monthly income over the 6 calendar months before filing. This includes wages, salary, commissions, bonuses, self-employment income, rental income, and regular contributions from others.")],
    """<div class="hero"><div class="container">
<h1>The Bankruptcy Means Test in Atlanta</h1>
<p class="subtitle">The means test determines whether you qualify for Chapter 7 bankruptcy in the Northern District of Georgia. Here is how it works and what income thresholds apply to Atlanta-area filers.</p>
</div></div>

<section><div class="container">
<h2>What Is the Means Test?</h2>
<div class="card">
<p>The means test was created by the 2005 Bankruptcy Abuse Prevention and Consumer Protection Act (BAPCPA) to determine whether a debtor has enough disposable income to repay some debts through Chapter 13 instead of eliminating them through Chapter 7.</p>
<p>The test compares your household income to Georgia's median income for your household size. If your income is below the median, you pass automatically and can file Chapter 7. If above, a second calculation determines whether you have enough disposable income to fund a Chapter 13 plan.</p>
</div>
</div></section>

<section><div class="container">
<h2>2026 Georgia Median Income Thresholds</h2>
<div class="card">
<table>
<tr><th>Household Size</th><th>Annual Median Income</th><th>Monthly</th></tr>
<tr><td>1 person</td><td>$55,234</td><td>$4,603</td></tr>
<tr><td>2 people</td><td>$72,108</td><td>$6,009</td></tr>
<tr><td>3 people</td><td>$82,563</td><td>$6,880</td></tr>
<tr><td>4 people</td><td>$98,725</td><td>$8,227</td></tr>
</table>
<p style="margin-top:12px;color:#8b949e;font-size:0.9rem">Source: U.S. Census Bureau / DOJ. Thresholds are updated periodically. Confirm current figures with the <a href="https://www.justice.gov/ust/means-testing" target="_blank" rel="noopener">U.S. Trustee</a>.</p>
</div>
</div></section>

<section><div class="container">
<h2>Step-by-Step: How the Means Test Works</h2>
<div class="card">
<ol>
<li><strong>Calculate your Current Monthly Income (CMI).</strong> Add all income sources for the 6 full calendar months before filing, divide by 6.</li>
<li><strong>Compare to Georgia median.</strong> If your CMI times 12 is below the median for your household size, you pass. File Chapter 7.</li>
<li><strong>If above median, deduct allowed expenses.</strong> IRS Local Standards for housing and transportation, plus actual secured debt payments, taxes, insurance, and child care.</li>
<li><strong>Calculate disposable income.</strong> If your monthly disposable income is less than roughly $160/month (or less than $9,675 over 60 months), you pass the second part of the means test.</li>
</ol>
</div>
</div></section>

<section><div class="container">
<h2>What Income Counts?</h2>
<div class="card">
<p>The means test counts almost all income received in the 6 months before filing:</p>
<ul>
<li>Wages, salary, tips, commissions</li>
<li>Bonuses and overtime</li>
<li>Self-employment and business income</li>
<li>Rental and investment income</li>
<li>Pension and retirement distributions</li>
<li>Regular contributions from household members</li>
<li>Unemployment compensation</li>
</ul>
<p><strong>Not counted:</strong> Social Security benefits, payments to victims of war crimes or terrorism, and certain disability payments.</p>
</div>
</div></section>

<section><div class="container">
<h2>What If I Fail?</h2>
<div class="card">
<p>Failing the means test does not end your options:</p>
<ul>
<li><strong>Chapter 13 has no income limit.</strong> You can file Chapter 13 regardless of income. <a href="/atlanta/chapter-13.html">Atlanta Chapter 13 guide</a>.</li>
<li><strong>Special circumstances.</strong> Military service members, disabled veterans, and reservists may qualify for exemptions from the means test.</li>
<li><strong>Timing matters.</strong> If your income dropped recently (job loss, pay cut), waiting a few months can change your 6-month average and help you qualify.</li>
</ul>
<p><a href="https://bankruptcymeanstest.org" target="_blank" rel="noopener">Full means test guide at bankruptcymeanstest.org</a></p>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>What is the means test for Atlanta bankruptcy?</summary><div class="answer"><p>The means test compares your household income to Georgia's median. For a single filer, the 2026 Georgia median is approximately $55,000. If below, you automatically qualify for Chapter 7. If above, you may still qualify after deducting allowed expenses. <a href="https://bankruptcymeanstest.org">Full guide</a>.</p></div></details>
<details class="faq-item"><summary>What if I fail the means test?</summary><div class="answer"><p>You can still file Chapter 13, which has no income limit. You may also qualify for Chapter 7 after deducting allowed expenses, or if special circumstances apply (military service, disability).</p></div></details>
<details class="faq-item"><summary>What income counts for the means test?</summary><div class="answer"><p>Almost all income over the 6 calendar months before filing, including wages, self-employment, rental income, and regular contributions. Social Security benefits are excluded.</p></div></details>
</div></section>"""
)
if write_if_missing("atlanta/means-test.html", html): created += 1

# automatic-stay
html = page(
    "Automatic Stay in Atlanta Bankruptcy -- 2026 Guide | Georgia Bankruptcy",
    "How the automatic stay protects Atlanta filers from foreclosure, repossession, garnishment, and creditor harassment the moment you file bankruptcy in N.D. Ga.",
    "https://georgiabankruptcy.org/atlanta/automatic-stay.html",
    ATL_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Atlanta","https://georgiabankruptcy.org/atlanta/"),("Automatic Stay","https://georgiabankruptcy.org/atlanta/automatic-stay.html")],
    [("What is the automatic stay?","The automatic stay is a federal injunction that takes effect the instant you file bankruptcy. It stops foreclosure, repossession, wage garnishment, lawsuits, and creditor phone calls. Creditors who violate the stay can be held in contempt of court."),
     ("How long does the automatic stay last?","In a Chapter 7 case, the stay lasts until your case is closed or your discharge is entered (typically 3-4 months). In Chapter 13, the stay lasts for the duration of your 3-5 year plan. If you filed and had a case dismissed within the prior year, the stay may be limited to 30 days."),
     ("Can a creditor get around the automatic stay?","Yes, creditors can file a motion for relief from stay asking the court to allow foreclosure or repossession to proceed. This is most common for secured debts like mortgages and car loans when payments are not current.")],
    """<div class="hero"><div class="container">
<h1>The Automatic Stay in Atlanta Bankruptcy</h1>
<p class="subtitle">The moment you file bankruptcy in the Northern District of Georgia, the automatic stay stops foreclosure, repossession, wage garnishment, and creditor harassment. Here is how it protects Atlanta filers.</p>
</div></div>

<section><div class="container">
<h2>What the Automatic Stay Stops</h2>
<div class="card">
<p>Under 11 U.S.C. section 362, the <a href="https://automaticstay.org" target="_blank" rel="noopener">automatic stay</a> immediately halts:</p>
<ul>
<li><strong>Foreclosure</strong> -- Georgia is a non-judicial foreclosure state where sales can happen in as few as 60 days. The stay stops the sale instantly.</li>
<li><strong>Repossession</strong> -- Lenders cannot repossess your vehicle once your case is filed.</li>
<li><strong>Wage garnishment</strong> -- Existing garnishment orders are halted.</li>
<li><strong>Lawsuits</strong> -- Pending collection lawsuits are paused.</li>
<li><strong>Phone calls and letters</strong> -- Creditors must stop all collection contact.</li>
<li><strong>Utility disconnection</strong> -- Utilities cannot be shut off for 20 days after filing.</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>How Long Does the Stay Last?</h2>
<div class="card">
<table>
<tr><th>Situation</th><th>Duration</th></tr>
<tr><td>First bankruptcy filing (Chapter 7)</td><td>Until discharge or case closure (3-4 months)</td></tr>
<tr><td>First filing (Chapter 13)</td><td>Duration of plan (3-5 years)</td></tr>
<tr><td>Second filing within 1 year</td><td>30 days (unless extended by court order)</td></tr>
<tr><td>Third+ filing within 1 year</td><td>No automatic stay (must request from court)</td></tr>
</table>
<p style="margin-top:12px">If you had a case dismissed within the prior year, you should discuss timing strategy with an attorney before refiling.</p>
</div>
</div></section>

<section><div class="container">
<h2>Violations of the Automatic Stay</h2>
<div class="card">
<p>Creditors who continue collection activity after being notified of your bankruptcy filing are violating federal law. The court can award:</p>
<ul>
<li><strong>Actual damages</strong> -- financial losses caused by the violation</li>
<li><strong>Emotional distress damages</strong> -- for harassment or distress</li>
<li><strong>Punitive damages</strong> -- in egregious cases</li>
<li><strong>Attorney fees</strong> -- cost of enforcing the stay</li>
</ul>
<p>If a creditor continues calling, garnishing, or attempting to repossess after your filing, document every contact and notify the court.</p>
</div>
</div></section>

<section><div class="container">
<h2>Relief from Stay</h2>
<div class="card">
<p>Creditors can ask the court to lift the automatic stay by filing a motion for relief. This is most common when:</p>
<ul>
<li>You are behind on mortgage payments and have no plan to catch up</li>
<li>You are behind on car payments and the vehicle is depreciating</li>
<li>The creditor has no adequate protection for its collateral</li>
</ul>
<p>In Chapter 13, you can usually prevent relief from stay by proposing a plan that brings payments current. <a href="/atlanta/chapter-13.html">Atlanta Chapter 13 guide</a>.</p>
</div>
</div></section>

<section><div class="container">
<h2>Georgia-Specific: Non-Judicial Foreclosure</h2>
<div class="card">
<p>Because Georgia allows non-judicial foreclosure, your lender can schedule a foreclosure sale without going to court. This makes the automatic stay especially critical for Atlanta homeowners -- it is often the only thing standing between you and loss of your home.</p>
<p>If you are facing foreclosure, filing before the sale date triggers the stay and stops the sale. <a href="/atlanta/keep-your-house.html">How to keep your house in Atlanta bankruptcy</a>.</p>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>What is the automatic stay?</summary><div class="answer"><p>The automatic stay is a federal injunction under 11 U.S.C. section 362 that takes effect the instant you file bankruptcy. It stops foreclosure, repossession, garnishment, lawsuits, and creditor contact. <a href="https://automaticstay.org">Full guide</a>.</p></div></details>
<details class="faq-item"><summary>How long does the automatic stay last?</summary><div class="answer"><p>For a first-time filer, the stay lasts until discharge (3-4 months in Chapter 7, 3-5 years in Chapter 13). If you had a case dismissed in the prior year, the stay may be limited to 30 days.</p></div></details>
<details class="faq-item"><summary>Can a creditor get around the automatic stay?</summary><div class="answer"><p>Yes. Creditors can file a motion for relief from stay. This is most common for secured debts like mortgages and car loans when payments are not being made.</p></div></details>
</div></section>"""
)
if write_if_missing("atlanta/automatic-stay.html", html): created += 1

# keep-your-car
html = page(
    "Keep Your Car in Atlanta Bankruptcy -- 2026 Guide | Georgia Bankruptcy",
    "How to keep your vehicle when filing bankruptcy in Atlanta. Georgia's $5,000 vehicle exemption, reaffirmation, redemption, and cramdown options in N.D. Ga.",
    "https://georgiabankruptcy.org/atlanta/keep-your-car.html",
    ATL_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Atlanta","https://georgiabankruptcy.org/atlanta/"),("Keep Your Car","https://georgiabankruptcy.org/atlanta/keep-your-car.html")],
    [("Can I keep my car if I file bankruptcy in Atlanta?","Georgia's vehicle exemption protects up to $5,000 of equity in one motor vehicle. If you owe more than the car is worth or your equity is under $5,000, you can typically keep it. The wildcard exemption can protect additional equity."),
     ("What is reaffirmation?","Reaffirmation is an agreement to keep paying a car loan through bankruptcy. You sign a new contract with the lender agreeing to remain personally liable for the debt. The car is not discharged, but you keep it."),
     ("What is cramdown in Chapter 13?","If you purchased your vehicle more than 910 days before filing, Chapter 13 lets you pay the car's current market value instead of the full loan balance. This can save thousands on an underwater car loan.")],
    """<div class="hero"><div class="container">
<h1>Keep Your Car in Atlanta Bankruptcy</h1>
<p class="subtitle">Most Atlanta filers can keep their vehicle in bankruptcy. Georgia's $5,000 vehicle exemption, plus reaffirmation and cramdown options, give you multiple paths to protect your car.</p>
</div></div>

<section><div class="container">
<h2>Georgia's Vehicle Exemption</h2>
<div class="card">
<p>Georgia exempts up to <strong>$5,000 of equity</strong> in one motor vehicle per filer (O.C.G.A. section 44-13-100(a)(3)). Equity is your car's market value minus what you owe on it.</p>
<table>
<tr><th>Scenario</th><th>Can You Keep It?</th></tr>
<tr><td>Car worth $8,000, owe $6,000 (equity $2,000)</td><td>Yes -- equity under $5,000</td></tr>
<tr><td>Car worth $15,000, owe $12,000 (equity $3,000)</td><td>Yes -- equity under $5,000</td></tr>
<tr><td>Car worth $20,000, owe $10,000 (equity $10,000)</td><td>Need wildcard or Chapter 13</td></tr>
<tr><td>Car worth $5,000, owe $8,000 (underwater)</td><td>Yes -- no equity to protect</td></tr>
</table>
<p style="margin-top:12px">The <strong>wildcard exemption</strong> ($600 plus up to $5,000 of unused homestead) can protect additional vehicle equity beyond the $5,000 limit.</p>
</div>
</div></section>

<section><div class="container">
<h2>Options for Keeping Your Car</h2>
<div class="card">
<h3>Chapter 7 Options</h3>
<ul>
<li><strong>Reaffirmation:</strong> Sign a new agreement to keep paying the loan. You keep the car but remain personally liable for the debt.</li>
<li><strong>Redemption:</strong> Pay the lender the car's current market value in a lump sum. Useful when you owe much more than the car is worth.</li>
<li><strong>Surrender:</strong> Give the car back and eliminate the remaining loan balance through discharge.</li>
</ul>
</div>
<div class="card">
<h3>Chapter 13 Options</h3>
<ul>
<li><strong>Cramdown:</strong> If you bought the car more than 910 days before filing, you can pay only the car's current value (not the full loan balance) through your plan at a court-approved interest rate.</li>
<li><strong>Cure arrears:</strong> Catch up on missed payments through your 3-5 year plan while keeping the vehicle.</li>
<li><strong>Reduce interest rate:</strong> The court can reduce your car loan interest rate to a market rate (typically prime + 1-3%).</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>The 910-Day Rule</h2>
<div class="card">
<p>If you purchased your vehicle within 910 days (about 2.5 years) of filing, the cramdown option is not available. You must pay the full loan balance through your Chapter 13 plan. This is called the "hanging paragraph" rule under 11 U.S.C. section 1325(a).</p>
<p>If you purchased the vehicle <strong>more than 910 days</strong> before filing, cramdown can save you significant money on an underwater car loan.</p>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>Can I keep my car if I file bankruptcy in Atlanta?</summary><div class="answer"><p>Most likely yes. Georgia's $5,000 vehicle exemption covers your equity. If you owe more than the car is worth, you have no equity to protect. The wildcard exemption provides additional coverage. <a href="https://keepmycarinbankruptcy.com">Full car guide</a>.</p></div></details>
<details class="faq-item"><summary>What is reaffirmation?</summary><div class="answer"><p>A reaffirmation agreement is a new contract with your lender agreeing to keep paying the car loan through bankruptcy. You keep the car but remain personally liable.</p></div></details>
<details class="faq-item"><summary>What is cramdown in Chapter 13?</summary><div class="answer"><p>Cramdown lets you pay only the car's current market value instead of the full loan balance, if you bought the car more than 910 days before filing. This can save thousands.</p></div></details>
</div></section>"""
)
if write_if_missing("atlanta/keep-your-car.html", html): created += 1

# keep-your-house
html = page(
    "Keep Your House in Atlanta Bankruptcy -- 2026 Guide | Georgia Bankruptcy",
    "How to keep your home when filing bankruptcy in Atlanta. Georgia's $21,500 homestead exemption, stopping foreclosure with Chapter 13, and the automatic stay.",
    "https://georgiabankruptcy.org/atlanta/keep-your-house.html",
    ATL_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Atlanta","https://georgiabankruptcy.org/atlanta/"),("Keep Your House","https://georgiabankruptcy.org/atlanta/keep-your-house.html")],
    [("Will I lose my house if I file bankruptcy in Atlanta?","Georgia's homestead exemption protects up to $21,500 of equity in your primary residence ($43,000 for married couples filing jointly). If your equity is within these limits, you can keep your home in Chapter 7. Chapter 13 lets you keep your home while catching up on missed payments over 3-5 years."),
     ("How does Chapter 13 stop foreclosure?","Filing Chapter 13 triggers the automatic stay, which immediately halts foreclosure. Your plan then allows you to catch up on missed mortgage payments over 3-5 years while making current payments going forward."),
     ("Can I strip a second mortgage in Chapter 13?","If your home is worth less than what you owe on your first mortgage, a second mortgage or HELOC may be treated as unsecured debt and eliminated through your Chapter 13 plan. This is called lien stripping.")],
    """<div class="hero"><div class="container">
<h1>Keep Your House in Atlanta Bankruptcy</h1>
<p class="subtitle">Georgia is a non-judicial foreclosure state where lenders can sell your home in as few as 60 days. Bankruptcy can stop foreclosure and give you time to catch up. Here is how Atlanta homeowners protect their property.</p>
</div></div>

<section><div class="container">
<h2>Georgia's Homestead Exemption</h2>
<div class="card">
<p>Georgia's homestead exemption protects up to <strong>$21,500</strong> of equity in your primary residence (O.C.G.A. section 44-13-100(a)(1)). For married couples filing jointly, the exemption doubles to <strong>$43,000</strong>.</p>
<p>Equity is your home's market value minus what you owe on all mortgages and liens. If your equity is within the exemption, you keep your home.</p>
<table>
<tr><th>Home Value</th><th>Mortgage Balance</th><th>Equity</th><th>Protected?</th></tr>
<tr><td>$250,000</td><td>$240,000</td><td>$10,000</td><td>Yes -- under $21,500</td></tr>
<tr><td>$300,000</td><td>$260,000</td><td>$40,000</td><td>Joint filers: yes. Single: need Chapter 13</td></tr>
<tr><td>$200,000</td><td>$210,000</td><td>$0 (underwater)</td><td>Yes -- no equity</td></tr>
</table>
</div>
</div></section>

<section><div class="container">
<h2>Chapter 13: The Foreclosure Defense</h2>
<div class="card">
<p>Chapter 13 is the primary tool for saving a home from foreclosure in Atlanta:</p>
<ul>
<li><strong>The <a href="https://automaticstay.org">automatic stay</a> stops foreclosure immediately</strong> -- even if a sale date is already scheduled</li>
<li><strong>Cure mortgage arrears</strong> over 3-5 years through your repayment plan while making current payments going forward</li>
<li><strong>Lien stripping:</strong> If your home is worth less than your first mortgage balance, a second mortgage or HELOC can be treated as unsecured debt and eliminated</li>
<li><strong>Keep your home</strong> as long as you complete the plan and make all required payments</li>
</ul>
<p style="color:#f85149"><strong>Warning:</strong> The Northern District has a 72.9% Chapter 13 dismissal rate. Make sure your budget can sustain 3-5 years of plan payments before filing.</p>
</div>
</div></section>

<section><div class="container">
<h2>Chapter 7 and Your Home</h2>
<div class="card">
<p>Chapter 7 can help homeowners too, but in a more limited way:</p>
<ul>
<li>If your equity is within the $21,500 homestead exemption, you keep your home</li>
<li>Chapter 7 eliminates unsecured debt (credit cards, medical bills), freeing up money for mortgage payments</li>
<li>The automatic stay provides temporary relief from foreclosure during the case (3-4 months)</li>
<li>Chapter 7 does <strong>not</strong> cure mortgage arrears -- you must negotiate with your lender separately</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>Non-Judicial Foreclosure in Georgia</h2>
<div class="card">
<p>Georgia does not require lenders to go to court to foreclose. The process can move fast:</p>
<ol>
<li><strong>Default:</strong> Miss a payment and the lender sends a demand letter</li>
<li><strong>Notice:</strong> Lender publishes notice of sale in the county newspaper for 4 consecutive weeks</li>
<li><strong>Sale:</strong> Foreclosure sale held on the first Tuesday of any month at the county courthouse</li>
</ol>
<p>From first missed payment to sale can be as few as <strong>60 days</strong>. If you are behind on your mortgage, time is critical. Filing bankruptcy before the sale date triggers the automatic stay and stops the process.</p>
<p><a href="https://foreclosurebankruptcy.com" target="_blank" rel="noopener">Learn more about foreclosure and bankruptcy</a> | <a href="https://keepmyhouseinbankruptcy.com" target="_blank" rel="noopener">keepmyhouseinbankruptcy.com</a></p>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>Will I lose my house if I file bankruptcy?</summary><div class="answer"><p>Most Atlanta homeowners keep their homes. Georgia's $21,500 homestead exemption ($43,000 for married couples) protects your equity. Chapter 13 can stop foreclosure and let you catch up on missed payments.</p></div></details>
<details class="faq-item"><summary>How does Chapter 13 stop foreclosure?</summary><div class="answer"><p>Filing triggers the automatic stay, which halts foreclosure immediately. Your Chapter 13 plan then allows you to cure missed payments over 3-5 years while making current payments.</p></div></details>
<details class="faq-item"><summary>Can I strip a second mortgage?</summary><div class="answer"><p>If your home is worth less than what you owe on your first mortgage, a second mortgage may be treated as unsecured debt in Chapter 13 and eliminated when you complete your plan.</p></div></details>
</div></section>"""
)
if write_if_missing("atlanta/keep-your-house.html", html): created += 1

# medical-debt
html = page(
    "Medical Debt Bankruptcy in Atlanta -- 2026 Guide | Georgia Bankruptcy",
    "How bankruptcy eliminates medical debt for Atlanta residents. Chapter 7 and Chapter 13 options, hospital liens, collections, and Georgia's exemptions.",
    "https://georgiabankruptcy.org/atlanta/medical-debt.html",
    ATL_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Atlanta","https://georgiabankruptcy.org/atlanta/"),("Medical Debt","https://georgiabankruptcy.org/atlanta/medical-debt.html")],
    [("Can I eliminate medical debt in bankruptcy?","Yes. Medical debt is unsecured debt and is fully dischargeable in both Chapter 7 and Chapter 13. In Chapter 7, medical bills are eliminated in 3-4 months. In Chapter 13, you may pay a small percentage through your plan."),
     ("Will medical debt bankruptcy affect my credit?","Bankruptcy stays on your credit report for 7 years (Chapter 13) or 10 years (Chapter 7). However, most people who file for medical debt already have damaged credit from collections and late payments. Many filers see their credit score improve within 1-2 years after discharge."),
     ("How much medical debt do I need to file bankruptcy?","There is no minimum amount of debt required to file bankruptcy. However, the costs of filing (attorney fees, filing fees) should be weighed against the amount of debt. Many attorneys offer free consultations to help you decide.")],
    """<div class="hero"><div class="container">
<h1>Eliminate Medical Debt Through Atlanta Bankruptcy</h1>
<p class="subtitle">Medical bills are the leading cause of bankruptcy filings in the United States. Both Chapter 7 and Chapter 13 can eliminate medical debt for Atlanta residents.</p>
</div></div>

<section><div class="container">
<h2>Medical Debt Is Fully Dischargeable</h2>
<div class="card">
<p>Medical debt is classified as <strong>unsecured, non-priority debt</strong> -- the same category as credit cards and personal loans. This means it is fully dischargeable in bankruptcy.</p>
<ul>
<li><strong>Chapter 7:</strong> Medical debt is eliminated entirely in 3-4 months</li>
<li><strong>Chapter 13:</strong> Medical debt is included as unsecured debt in your plan. You pay whatever your disposable income allows, and the remaining balance is discharged at completion.</li>
</ul>
<p>There is no limit on how much medical debt can be discharged.</p>
</div>
</div></section>

<section><div class="container">
<h2>Hospital Liens and Judgments</h2>
<div class="card">
<p>Georgia law allows hospitals to place liens on personal injury settlements, but not on your other property. However, if a hospital or collection agency has obtained a <strong>judgment</strong> against you, they can garnish wages or levy bank accounts.</p>
<p>Filing bankruptcy stops all collection activity through the <a href="https://automaticstay.org">automatic stay</a>:</p>
<ul>
<li>Wage garnishment for medical debt stops immediately</li>
<li>Bank levies are halted</li>
<li>Collection calls and letters must cease</li>
<li>Pending lawsuits are paused</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>Chapter 7 vs. Chapter 13 for Medical Debt</h2>
<div class="card">
<table>
<tr><th>Factor</th><th>Chapter 7</th><th>Chapter 13</th></tr>
<tr><td>Timeline</td><td>3-4 months to discharge</td><td>3-5 year plan</td></tr>
<tr><td>Medical debt eliminated</td><td>100%</td><td>Varies (often pennies on the dollar)</td></tr>
<tr><td>Means test required</td><td>Yes</td><td>No</td></tr>
<tr><td>Keep all property</td><td>If within exemptions</td><td>Yes</td></tr>
<tr><td>Best for</td><td>Lower income, few assets</td><td>Higher income, property to protect</td></tr>
</table>
</div>
</div></section>

<section><div class="container">
<h2>Before You File: Other Options</h2>
<div class="card">
<ul>
<li><strong>Negotiate directly.</strong> Many hospitals will reduce bills by 30-50% for uninsured or underinsured patients.</li>
<li><strong>Charity care programs.</strong> Most Georgia hospitals have financial assistance programs for low-income patients. Grady Memorial Hospital in Atlanta has one of the state's largest programs.</li>
<li><strong>Medical debt and credit reporting.</strong> As of 2023, paid medical debts are removed from credit reports. Unpaid medical debts under $500 are also excluded.</li>
<li><strong>Statute of limitations.</strong> In Georgia, the statute of limitations on medical debt is 6 years. After that, creditors cannot sue to collect.</li>
</ul>
<p>If negotiation and charity care are not enough, bankruptcy provides a complete fresh start.</p>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>Can I eliminate medical debt in bankruptcy?</summary><div class="answer"><p>Yes. Medical debt is fully dischargeable in both Chapter 7 and Chapter 13. In Chapter 7, it is eliminated in 3-4 months. In Chapter 13, you may pay a small percentage through your plan.</p></div></details>
<details class="faq-item"><summary>Will medical debt bankruptcy affect my credit?</summary><div class="answer"><p>Bankruptcy stays on your credit report for 7-10 years. However, many filers with medical debt already have damaged credit. Most see improvement within 1-2 years after discharge. <a href="/atlanta/credit-after-bankruptcy.html">Credit rebuilding guide</a>.</p></div></details>
<details class="faq-item"><summary>How much medical debt do I need to file?</summary><div class="answer"><p>There is no minimum. Weigh filing costs against debt amount. Many attorneys offer free consultations.</p></div></details>
</div></section>"""
)
if write_if_missing("atlanta/medical-debt.html", html): created += 1

# 341-meeting
html = page(
    "341 Meeting of Creditors in Atlanta -- 2026 Guide | Georgia Bankruptcy",
    "What to expect at your 341 meeting of creditors in the Northern District of Georgia. Location, timing, questions asked, and how to prepare.",
    "https://georgiabankruptcy.org/atlanta/341-meeting.html",
    ATL_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Atlanta","https://georgiabankruptcy.org/atlanta/"),("341 Meeting","https://georgiabankruptcy.org/atlanta/341-meeting.html")],
    [("What happens at a 341 meeting in Atlanta?","The 341 meeting is a brief hearing where the bankruptcy trustee asks you questions about your finances, assets, and bankruptcy petition. It typically lasts 5-10 minutes. Creditors may attend but rarely do. The meeting is held at the N.D. Ga. courthouse or by phone/video."),
     ("What questions are asked at the 341 meeting?","The trustee will ask standard questions: Did you list all your assets? Is your petition accurate? Have you transferred any property recently? Do you have any pending lawsuits? Are you current on tax filings? The questions are straightforward if your petition is accurate."),
     ("What documents do I need for the 341 meeting?","Bring a government-issued photo ID (driver's license or passport) and proof of Social Security number (SS card, W-2, or 1099). Your attorney will advise if additional documents are needed.")],
    """<div class="hero"><div class="container">
<h1>The 341 Meeting of Creditors in Atlanta</h1>
<p class="subtitle">About 30 days after filing, you will attend a <a href="https://341meeting.org" style="color:#58a6ff">341 meeting of creditors</a>. This brief hearing is a routine part of every bankruptcy case in the Northern District of Georgia.</p>
</div></div>

<section><div class="container">
<h2>What Is the 341 Meeting?</h2>
<div class="card">
<p>The 341 meeting (named after 11 U.S.C. section 341) is a required hearing where the bankruptcy trustee reviews your case. Despite the name, creditors rarely attend. The meeting is not held before a judge.</p>
<ul>
<li><strong>Timing:</strong> Approximately 30 days after filing</li>
<li><strong>Duration:</strong> Typically 5-10 minutes</li>
<li><strong>Location:</strong> N.D. Ga. courthouse at 75 Ted Turner Dr SW, Atlanta, GA 30303, or by phone/video</li>
<li><strong>Who attends:</strong> You, your attorney (if you have one), and the bankruptcy trustee</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>What to Bring</h2>
<div class="card">
<ul>
<li><strong>Government-issued photo ID</strong> -- driver's license, state ID, or passport</li>
<li><strong>Proof of Social Security number</strong> -- Social Security card, W-2, or 1099 showing your full SSN</li>
<li><strong>Recent pay stubs</strong> -- last 60 days of pay stubs (your attorney may have already filed these)</li>
<li><strong>Recent bank statements</strong> -- the trustee may request these</li>
<li><strong>Tax returns</strong> -- most recent year's federal and state tax return</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>Typical Questions the Trustee Will Ask</h2>
<div class="card">
<ol>
<li>Did you read your bankruptcy petition before signing it?</li>
<li>Is everything in your petition true and correct?</li>
<li>Did you list all of your assets?</li>
<li>Did you list all of your debts?</li>
<li>Have you transferred any property in the last 2 years?</li>
<li>Are you expecting any tax refunds, inheritance, or lawsuit settlements?</li>
<li>Is anyone holding property for you?</li>
<li>Have you previously filed bankruptcy?</li>
<li>Are you current on domestic support obligations (child support/alimony)?</li>
<li>Have you filed all required tax returns?</li>
</ol>
<p style="margin-top:12px">Answer honestly and briefly. The trustee is not trying to trap you -- they are verifying your petition is accurate.</p>
</div>
</div></section>

<section><div class="container">
<h2>Tips for a Smooth 341 Meeting</h2>
<div class="card">
<ul>
<li><strong>Be honest.</strong> The meeting is conducted under oath. Inaccurate statements can jeopardize your case.</li>
<li><strong>Be brief.</strong> Answer the question asked, nothing more.</li>
<li><strong>Dress appropriately.</strong> Business casual is fine. You are not appearing before a judge.</li>
<li><strong>Arrive early.</strong> Give yourself time to find parking and the meeting room.</li>
<li><strong>Do not panic.</strong> The vast majority of 341 meetings are routine. If your petition is accurate, there is nothing to worry about.</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>After the 341 Meeting</h2>
<div class="card">
<p>After the meeting:</p>
<ul>
<li><strong>Chapter 7:</strong> Discharge typically enters about 60 days after the 341 meeting (approximately 90 days total from filing)</li>
<li><strong>Chapter 13:</strong> Your case proceeds to plan confirmation. The trustee will review your proposed plan and any creditor objections.</li>
</ul>
<p>In some cases, the trustee may continue (postpone) the 341 meeting to request additional documents. This is not unusual and does not mean there is a problem with your case.</p>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>What happens at a 341 meeting in Atlanta?</summary><div class="answer"><p>The trustee asks you questions about your finances and petition under oath. It lasts 5-10 minutes. Creditors may attend but rarely do. <a href="https://341meeting.org">Full 341 meeting guide</a>.</p></div></details>
<details class="faq-item"><summary>What questions are asked?</summary><div class="answer"><p>Standard questions about whether your petition is accurate, whether you listed all assets and debts, and whether you have transferred property recently. The questions are straightforward.</p></div></details>
<details class="faq-item"><summary>What documents do I need?</summary><div class="answer"><p>Photo ID and proof of Social Security number are required. Bring recent pay stubs, bank statements, and tax returns as well.</p></div></details>
</div></section>"""
)
if write_if_missing("atlanta/341-meeting.html", html): created += 1

# timeline
html = page(
    "Atlanta Bankruptcy Timeline -- Step by Step 2026 Guide | Georgia Bankruptcy",
    "Step-by-step bankruptcy timeline for Atlanta filers. From consultation to discharge, what to expect in Chapter 7 and Chapter 13 in the Northern District of Georgia.",
    "https://georgiabankruptcy.org/atlanta/timeline.html",
    ATL_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Atlanta","https://georgiabankruptcy.org/atlanta/"),("Timeline","https://georgiabankruptcy.org/atlanta/timeline.html")],
    [("How long does Chapter 7 take in Atlanta?","Most Chapter 7 cases in the Northern District of Georgia take 3-4 months from filing to discharge. The 341 meeting occurs about 30 days after filing, and discharge follows approximately 60 days later."),
     ("How long does Chapter 13 take?","Chapter 13 requires completing a 3-5 year repayment plan. The plan is typically confirmed 2-4 months after filing. Discharge occurs after all plan payments are made."),
     ("How long before the automatic stay takes effect?","The automatic stay takes effect the instant your case is filed. If filed electronically, this can be within hours of your attorney preparing the petition.")],
    """<div class="hero"><div class="container">
<h1>Atlanta Bankruptcy Timeline</h1>
<p class="subtitle">From your first consultation to discharge, here is what to expect at each stage of the bankruptcy process in the Northern District of Georgia.</p>
</div></div>

<section><div class="container">
<h2>Chapter 7 Timeline</h2>
<div class="card">
<table>
<tr><th>Stage</th><th>When</th><th>What Happens</th></tr>
<tr><td>Pre-filing credit counseling</td><td>Before filing</td><td>Complete an approved credit counseling course (usually online, 1-2 hours). Required within 180 days before filing.</td></tr>
<tr><td>Filing day</td><td>Day 0</td><td>Petition filed with N.D. Ga. Automatic stay takes effect immediately. All collection activity must stop.</td></tr>
<tr><td>341 Meeting</td><td>~30 days</td><td>Brief meeting with the trustee. Bring ID and proof of SSN. <a href="/atlanta/341-meeting.html">341 meeting guide</a>.</td></tr>
<tr><td>Objection deadline</td><td>~60 days</td><td>Creditors have 60 days after the 341 meeting to object to discharge of specific debts.</td></tr>
<tr><td>Post-filing debtor education</td><td>Before discharge</td><td>Complete a second required course (financial management). Usually online, 2 hours.</td></tr>
<tr><td>Discharge</td><td>~90 days</td><td>Court enters discharge order eliminating eligible debts.</td></tr>
<tr><td>Case closed</td><td>~120 days</td><td>Trustee files final report and case is closed.</td></tr>
</table>
</div>
</div></section>

<section><div class="container">
<h2>Chapter 13 Timeline</h2>
<div class="card">
<table>
<tr><th>Stage</th><th>When</th><th>What Happens</th></tr>
<tr><td>Pre-filing credit counseling</td><td>Before filing</td><td>Same requirement as Chapter 7.</td></tr>
<tr><td>Filing day</td><td>Day 0</td><td>Petition and proposed plan filed. Automatic stay takes effect. First plan payment due within 30 days.</td></tr>
<tr><td>341 Meeting</td><td>~30 days</td><td>Trustee reviews your case and plan.</td></tr>
<tr><td>Plan confirmation</td><td>2-4 months</td><td>Judge approves your repayment plan after reviewing trustee and creditor objections.</td></tr>
<tr><td>Plan payments</td><td>3-5 years</td><td>Monthly payments to the Chapter 13 trustee, who distributes to creditors.</td></tr>
<tr><td>Post-filing debtor education</td><td>Before discharge</td><td>Complete the second required course.</td></tr>
<tr><td>Discharge</td><td>3-5 years</td><td>After completing all plan payments, remaining unsecured debt is discharged.</td></tr>
</table>
<p style="margin-top:12px;color:#f85149"><strong>Note:</strong> The N.D. Ga. has a 72.9% Chapter 13 dismissal rate. Many cases are dismissed before reaching discharge, often for missed plan payments.</p>
</div>
</div></section>

<section><div class="container">
<h2>Key Deadlines After Filing</h2>
<div class="card">
<ul>
<li><strong>30 days:</strong> First Chapter 13 plan payment due</li>
<li><strong>30-45 days:</strong> 341 meeting of creditors</li>
<li><strong>45 days after 341:</strong> Deadline for debtor to file tax returns (if not already filed)</li>
<li><strong>60 days after 341:</strong> Deadline for creditors to object to discharge (Chapter 7)</li>
<li><strong>Before discharge:</strong> Must complete debtor education course and file certificate with court</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>How long does Chapter 7 take in Atlanta?</summary><div class="answer"><p>Most Chapter 7 cases take 3-4 months from filing to discharge. The 341 meeting is at ~30 days, and discharge follows ~60 days after that.</p></div></details>
<details class="faq-item"><summary>How long does Chapter 13 take?</summary><div class="answer"><p>Chapter 13 requires completing a 3-5 year repayment plan. Plan confirmation typically happens 2-4 months after filing. Discharge occurs after all payments are made.</p></div></details>
<details class="faq-item"><summary>When does the automatic stay take effect?</summary><div class="answer"><p>Instantly upon filing. If filed electronically, this happens within hours of preparation. <a href="/atlanta/automatic-stay.html">Automatic stay guide</a>.</p></div></details>
</div></section>"""
)
if write_if_missing("atlanta/timeline.html", html): created += 1

# checklist
html = page(
    "Atlanta Bankruptcy Filing Checklist -- 2026 Guide | Georgia Bankruptcy",
    "Complete checklist of documents and information you need before filing bankruptcy in Atlanta. Prepare for your N.D. Ga. filing with this step-by-step list.",
    "https://georgiabankruptcy.org/atlanta/checklist.html",
    ATL_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Atlanta","https://georgiabankruptcy.org/atlanta/"),("Checklist","https://georgiabankruptcy.org/atlanta/checklist.html")],
    [("What documents do I need to file bankruptcy in Atlanta?","You need 6 months of pay stubs, 2 years of tax returns, bank statements, a list of all debts and creditors, a list of all assets and their values, vehicle titles, mortgage statements, and proof of credit counseling completion."),
     ("Do I need to take a class before filing?","Yes. Federal law requires two courses: a credit counseling course before filing and a debtor education course after filing. Both are available online and typically cost $15-25 each."),
     ("How do I find the right attorney?","Look for a bankruptcy attorney who regularly practices in the Northern District of Georgia. Ask about their dismissal rate, experience, and whether they offer a free consultation. Avoid firms that guarantee results or pressure you into filing quickly.")],
    """<div class="hero"><div class="container">
<h1>Atlanta Bankruptcy Filing Checklist</h1>
<p class="subtitle">Gather these documents and information before filing bankruptcy in the Northern District of Georgia. Being prepared helps your case go smoothly and reduces the risk of delays.</p>
</div></div>

<section><div class="container">
<h2>Documents You Need</h2>
<div class="card">
<h3>Income Documentation</h3>
<ul>
<li>Pay stubs for the last 6 months</li>
<li>Federal and state tax returns for the last 2 years</li>
<li>W-2s or 1099s for the last 2 years</li>
<li>Proof of any other income (Social Security, disability, rental income, child support received)</li>
<li>Profit and loss statements if self-employed</li>
</ul>
</div>
<div class="card">
<h3>Debt Documentation</h3>
<ul>
<li>Recent statements for all credit cards</li>
<li>Medical bills and collection notices</li>
<li>Mortgage statements (all mortgages and HELOCs)</li>
<li>Vehicle loan statements</li>
<li>Student loan statements</li>
<li>Personal loan and payday loan records</li>
<li>Any lawsuits, judgments, or garnishment orders</li>
<li>Tax debt notices from IRS or Georgia DOR</li>
</ul>
</div>
<div class="card">
<h3>Asset Documentation</h3>
<ul>
<li>Vehicle titles and registration</li>
<li>Property deed and most recent appraisal or tax assessment</li>
<li>Bank statements for all accounts (last 3-6 months)</li>
<li>Retirement account statements (401k, IRA, pension)</li>
<li>Life insurance policies with cash value</li>
<li>Investment account statements</li>
<li>List of valuable personal property (jewelry, electronics, collections)</li>
</ul>
</div>
<div class="card">
<h3>Other Items</h3>
<ul>
<li>Government-issued photo ID</li>
<li>Social Security card or proof of SSN</li>
<li>Credit counseling certificate (must complete before filing)</li>
<li>Divorce decree or separation agreement (if applicable)</li>
<li>Child support or alimony orders</li>
<li>Any prior bankruptcy case numbers and filing dates</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>Required Courses</h2>
<div class="card">
<table>
<tr><th>Course</th><th>When</th><th>Cost</th><th>Duration</th></tr>
<tr><td>Credit Counseling (pre-filing)</td><td>Within 180 days before filing</td><td>$15-25</td><td>1-2 hours</td></tr>
<tr><td>Debtor Education (post-filing)</td><td>After filing, before discharge</td><td>$15-25</td><td>2 hours</td></tr>
</table>
<p style="margin-top:12px">Both courses are available online from approved providers. The certificate must be filed with the court. A list of approved providers is available from the <a href="https://www.justice.gov/ust" target="_blank" rel="noopener">U.S. Trustee's website</a>.</p>
</div>
</div></section>

<section><div class="container">
<h2>Before You File: Key Questions to Ask</h2>
<div class="card">
<ol>
<li>Do I qualify for Chapter 7, or should I file Chapter 13? (<a href="/atlanta/means-test.html">Take the means test</a>)</li>
<li>Is my home equity within Georgia's $21,500 homestead exemption?</li>
<li>Is my vehicle equity within the $5,000 vehicle exemption?</li>
<li>Have I filed bankruptcy before? When? (<a href="https://1328f.com">Check eligibility</a>)</li>
<li>Am I current on child support and alimony?</li>
<li>Have I filed all required tax returns?</li>
<li>Have I transferred any property in the last 2 years?</li>
</ol>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>What documents do I need to file bankruptcy in Atlanta?</summary><div class="answer"><p>Pay stubs (6 months), tax returns (2 years), bank statements, all debt statements, asset values, vehicle titles, mortgage statements, and credit counseling certificate.</p></div></details>
<details class="faq-item"><summary>Do I need to take a class before filing?</summary><div class="answer"><p>Yes. Two courses are required: credit counseling before filing and debtor education after. Both are online, 1-2 hours, and cost $15-25 each.</p></div></details>
<details class="faq-item"><summary>How do I find the right attorney?</summary><div class="answer"><p>Look for experience in the N.D. Ga., ask about dismissal rates, and verify they offer a free consultation. Avoid firms that pressure you or guarantee outcomes.</p></div></details>
</div></section>"""
)
if write_if_missing("atlanta/checklist.html", html): created += 1

# credit-after-bankruptcy
html = page(
    "Rebuilding Credit After Bankruptcy in Atlanta -- 2026 Guide | Georgia Bankruptcy",
    "How to rebuild your credit after bankruptcy in Atlanta. Timeline, practical steps, secured cards, and what to expect for your credit score.",
    "https://georgiabankruptcy.org/atlanta/credit-after-bankruptcy.html",
    ATL_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Atlanta","https://georgiabankruptcy.org/atlanta/"),("Credit After Bankruptcy","https://georgiabankruptcy.org/atlanta/credit-after-bankruptcy.html")],
    [("How long does bankruptcy stay on my credit report?","Chapter 7 stays on your credit report for 10 years from the filing date. Chapter 13 stays for 7 years. However, the impact on your score decreases over time, and many people see significant improvement within 1-2 years after discharge."),
     ("Can I get a credit card after bankruptcy?","Yes. Secured credit cards are available almost immediately after discharge. A secured card requires a deposit (typically $200-500) that becomes your credit limit. Using the card responsibly and paying in full each month rebuilds your credit."),
     ("Can I buy a house after bankruptcy?","Yes, but there are waiting periods. FHA loans require a 2-year wait after Chapter 7 discharge or 1 year of on-time Chapter 13 payments. Conventional loans require 4 years after Chapter 7. VA loans require 2 years.")],
    """<div class="hero"><div class="container">
<h1>Rebuilding Credit After Bankruptcy in Atlanta</h1>
<p class="subtitle">Bankruptcy is not the end of your financial life -- it is the beginning of a fresh start. Most Atlanta filers see their credit score improve within 1-2 years of discharge. Here is how to rebuild.</p>
</div></div>

<section><div class="container">
<h2>How Long Bankruptcy Stays on Your Credit Report</h2>
<div class="card">
<table>
<tr><th>Chapter</th><th>Duration on Report</th><th>Score Impact Over Time</th></tr>
<tr><td>Chapter 7</td><td>10 years from filing</td><td>Heaviest impact years 1-2, diminishes after year 3</td></tr>
<tr><td>Chapter 13</td><td>7 years from filing</td><td>Diminishes steadily, especially after year 2</td></tr>
</table>
<p style="margin-top:12px">The practical reality: most people who file bankruptcy already have damaged credit from late payments, collections, and judgments. Many filers find their credit score is <strong>higher</strong> 12-18 months after discharge than it was before filing.</p>
</div>
</div></section>

<section><div class="container">
<h2>Step-by-Step Credit Rebuilding Plan</h2>
<div class="card">
<h3>Months 1-3 After Discharge</h3>
<ul>
<li>Pull your free credit reports from all 3 bureaus at <a href="https://www.annualcreditreport.com" target="_blank" rel="noopener">AnnualCreditReport.com</a></li>
<li>Dispute any debts that were discharged but still show as active or owing a balance</li>
<li>Apply for a <strong>secured credit card</strong> (deposit required, typically $200-500)</li>
<li>Set up a simple budget now that your debts are eliminated</li>
</ul>
</div>
<div class="card">
<h3>Months 3-12</h3>
<ul>
<li>Use the secured card for small purchases and pay the balance in full each month</li>
<li>Consider a credit-builder loan from a credit union (many Atlanta-area credit unions offer these)</li>
<li>Keep credit utilization below 30% of your limit</li>
<li>Pay all bills on time -- payment history is the largest factor in your credit score</li>
</ul>
</div>
<div class="card">
<h3>Year 1-2</h3>
<ul>
<li>Apply for an unsecured credit card when your score reaches the 620-650 range</li>
<li>Consider a small installment loan to diversify your credit mix</li>
<li>Continue perfect payment history</li>
<li>Begin saving for a down payment if homeownership is a goal</li>
</ul>
</div>
<div class="card">
<h3>Year 2+</h3>
<ul>
<li>You may qualify for an FHA mortgage (2 years after Chapter 7 discharge)</li>
<li>Auto loans become available at reasonable rates</li>
<li>Continue building positive credit history</li>
<li>Monitor your credit regularly for errors or identity theft</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>Buying a Home After Bankruptcy</h2>
<div class="card">
<table>
<tr><th>Loan Type</th><th>Wait After Ch. 7</th><th>Wait After Ch. 13</th></tr>
<tr><td>FHA</td><td>2 years from discharge</td><td>1 year of on-time plan payments (with court approval)</td></tr>
<tr><td>VA</td><td>2 years from discharge</td><td>1 year of on-time plan payments</td></tr>
<tr><td>USDA</td><td>3 years from discharge</td><td>1 year of on-time plan payments</td></tr>
<tr><td>Conventional</td><td>4 years from discharge</td><td>2 years from discharge</td></tr>
</table>
<p style="margin-top:12px"><a href="https://rebuildcreditafterbankruptcy.com" target="_blank" rel="noopener">More at rebuildcreditafterbankruptcy.com</a> | <a href="https://buyahouseafterbankruptcy.com" target="_blank" rel="noopener">buyahouseafterbankruptcy.com</a></p>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>How long does bankruptcy stay on my credit report?</summary><div class="answer"><p>Chapter 7: 10 years from filing. Chapter 13: 7 years from filing. The impact diminishes over time, with most improvement in the first 2 years after discharge.</p></div></details>
<details class="faq-item"><summary>Can I get a credit card after bankruptcy?</summary><div class="answer"><p>Yes. Secured credit cards are available almost immediately after discharge. Use it for small purchases and pay in full each month to rebuild your score.</p></div></details>
<details class="faq-item"><summary>Can I buy a house after bankruptcy?</summary><div class="answer"><p>Yes. FHA loans require 2 years after Chapter 7, or 1 year of on-time Chapter 13 payments. Conventional loans require 4 years after Chapter 7.</p></div></details>
</div></section>"""
)
if write_if_missing("atlanta/credit-after-bankruptcy.html", html): created += 1

# ============================================================
# ATLANTA SUBURBS - 10 pages
# ============================================================

suburbs = [
    ("marietta", "Marietta", "Cobb County", "30060"),
    ("roswell", "Roswell", "Fulton County", "30075"),
    ("alpharetta", "Alpharetta", "Fulton County", "30009"),
    ("sandy-springs", "Sandy Springs", "Fulton County", "30328"),
    ("decatur", "Decatur", "DeKalb County", "30030"),
    ("smyrna", "Smyrna", "Cobb County", "30080"),
    ("kennesaw", "Kennesaw", "Cobb County", "30144"),
    ("lawrenceville", "Lawrenceville", "Gwinnett County", "30046"),
    ("duluth-ga", "Duluth", "Gwinnett County", "30096"),
    ("stone-mountain", "Stone Mountain", "DeKalb County", "30083"),
]

for slug, name, county, zipcode in suburbs:
    html = page(
        f"Filing Bankruptcy in {name}, GA -- 2026 Guide | Georgia Bankruptcy",
        f"Free bankruptcy guide for {name}, Georgia ({county}) residents. File in the Northern District of Georgia. 72.9% Chapter 13 dismissal rate. Georgia exemptions, costs, and court info.",
        f"https://georgiabankruptcy.org/atlanta/suburbs/{slug}.html",
        f'<nav><div class="container"><a href="/atlanta/" class="brand">Atlanta Bankruptcy Guide</a><div class="links"><a href="/">Georgia</a><a href="/atlanta/">Atlanta</a><a href="/atlanta/suburbs/{slug}.html">{name}</a><a href="/atlanta/chapter-7.html">Chapter 7</a><a href="/atlanta/chapter-13.html">Chapter 13</a><a href="/atlanta/faq.html">FAQ</a></div></div></nav>',
        [("Georgia","https://georgiabankruptcy.org"),("Atlanta","https://georgiabankruptcy.org/atlanta/"),("Suburbs","https://georgiabankruptcy.org/atlanta/"),(name,f"https://georgiabankruptcy.org/atlanta/suburbs/{slug}.html")],
        [(f"Where do I file bankruptcy if I live in {name}?",f"{name} is in {county}, which is part of the Northern District of Georgia. You file at the U.S. Bankruptcy Court, 75 Ted Turner Dr SW, Atlanta, GA 30303. Phone: (404) 215-1000."),
         (f"How much does bankruptcy cost in {name}?","Filing fees are $338 for Chapter 7 and $313 for Chapter 13. Attorney fees in the Atlanta area typically range from $1,200 to $2,500 for Chapter 7 and $3,500 to $5,000 for Chapter 13. Two required credit counseling courses cost $25-$50 total."),
         (f"What is the dismissal rate for {name} bankruptcy cases?",f"{name} cases are filed in the Northern District of Georgia, which has a 72.9% Chapter 13 dismissal rate -- one of the highest in the nation. Nearly 3 out of 4 Chapter 13 cases fail to reach discharge.")],
        f"""<div class="hero"><div class="container">
<h1>Filing Bankruptcy in {name}, Georgia</h1>
<p class="subtitle">{name} residents in {county} file bankruptcy in the Northern District of Georgia. This guide covers Chapter 7, Chapter 13, Georgia exemptions, and what {name} filers need to know about the N.D. Ga. court.</p>
<div style="margin-top:16px;background:#f8514920;border:1px solid #f85149;border-radius:8px;padding:16px 24px;display:inline-block;color:#f85149;font-weight:600;font-size:1.05rem">N.D. Ga. has a 72.9% Chapter 13 dismissal rate</div>
</div></div>

<div class="container">
<div class="stats-row">
<div class="stat-card danger"><div class="number">72.9%</div><div class="label">Ch. 13 Dismissal Rate</div></div>
<div class="stat-card"><div class="number">$21,500</div><div class="label">Homestead Exemption</div></div>
<div class="stat-card"><div class="number">$5,000</div><div class="label">Vehicle Exemption</div></div>
<div class="stat-card"><div class="number">$338</div><div class="label">Ch. 7 Filing Fee</div></div>
</div>
</div>

<section><div class="container">
<h2>Where {name} Residents File</h2>
<div class="card">
<p>{name} is located in <strong>{county}</strong>, which is part of the <strong>Northern District of Georgia</strong>.</p>
<p><strong>Courthouse:</strong> U.S. Bankruptcy Court, 75 Ted Turner Dr SW, Atlanta, GA 30303</p>
<p><strong>Phone:</strong> (404) 215-1000</p>
<p><strong>Website:</strong> <a href="https://www.ganb.uscourts.gov" target="_blank" rel="noopener">ganb.uscourts.gov</a></p>
<p>All bankruptcy cases from {county} are handled at the Atlanta courthouse. The 341 meeting of creditors may be conducted in person at the courthouse or by phone/video.</p>
</div>
</div></section>

<section><div class="container">
<h2>Chapter 7 vs. Chapter 13 for {name} Residents</h2>
<div class="card">
<h3>Chapter 7 -- Fresh Start</h3>
<p>Chapter 7 eliminates most unsecured debts (credit cards, medical bills) in about 3-4 months. You must pass a <a href="https://meanstest.org" target="_blank" rel="noopener">means test</a> based on Georgia's median income.</p>
<ul>
<li>Discharge in 3-4 months</li>
<li>Filing fee: $338</li>
<li>Must pass the means test</li>
<li>Higher success rate than Chapter 13 in N.D. Ga.</li>
</ul>
<p><a href="/atlanta/chapter-7.html">Full Atlanta Chapter 7 guide</a></p>
</div>
<div class="card">
<h3>Chapter 13 -- Payment Plan</h3>
<p>Chapter 13 lets you keep property while repaying debts over 3-5 years. Good for saving a home from foreclosure.</p>
<ul>
<li>3-5 year repayment plan</li>
<li>Filing fee: $313</li>
<li>Keep your home and car</li>
<li style="color:#f85149"><strong>72.9% dismissal rate in N.D. Ga.</strong> -- choose your attorney carefully</li>
</ul>
<p><a href="/atlanta/chapter-13.html">Full Atlanta Chapter 13 guide</a></p>
</div>
</div></section>

<section><div class="container">
<h2>Georgia Exemptions</h2>
<div class="card">
<p>{name} filers use Georgia state exemptions (federal exemptions are not available in Georgia):</p>
<table>
<tr><th>Property</th><th>Exemption Amount</th></tr>
<tr><td>Homestead (primary residence)</td><td>$21,500 ($43,000 married filing jointly)</td></tr>
<tr><td>Vehicle</td><td>$5,000</td></tr>
<tr><td>Personal property</td><td>$600 per item, $5,000 aggregate</td></tr>
<tr><td>Wildcard</td><td>$600 + up to $5,000 of unused homestead</td></tr>
<tr><td>Retirement accounts</td><td>Fully exempt</td></tr>
<tr><td>Social Security</td><td>Fully exempt</td></tr>
</table>
<p style="margin-top:12px"><a href="/atlanta/exemptions.html">Full Georgia exemptions guide</a></p>
</div>
</div></section>

<section><div class="container">
<h2>Cost of Filing in {name}</h2>
<div class="card">
<ul>
<li><strong>Chapter 7 filing fee:</strong> $338</li>
<li><strong>Chapter 13 filing fee:</strong> $313</li>
<li><strong>Attorney fees (Atlanta area):</strong> $1,200 to $2,500 for Chapter 7; $3,500 to $5,000 for Chapter 13</li>
<li><strong>Credit counseling courses:</strong> $25-50 total (two required)</li>
</ul>
<p>Fee waivers are available for Chapter 7 filers below 150% of the federal poverty guidelines. Chapter 13 filing fees can be paid through your plan. <a href="/atlanta/cost.html">Full cost breakdown</a>.</p>
</div>
</div></section>

<section><div class="container">
<h2>The 72.9% Dismissal Rate Warning</h2>
<div class="card">
<p>The Northern District of Georgia has a <strong>72.9% Chapter 13 dismissal rate</strong>, meaning nearly 3 out of 4 Chapter 13 cases fail to reach discharge. Additionally, 44.8% of filers are repeat filers.</p>
<p>If you are considering Chapter 13 from {name}:</p>
<ul>
<li><strong>Choose your attorney carefully.</strong> Ask about their firm's completion rate.</li>
<li><strong>Make sure your budget works.</strong> The plan requires 3-5 years of consistent payments.</li>
<li><strong>Consider Chapter 7 first.</strong> If you qualify, it is faster and has a much higher success rate.</li>
</ul>
<p><a href="https://bankruptcydismissed.com" target="_blank" rel="noopener">What happens when a case is dismissed?</a></p>
</div>
</div></section>

<section><div class="container">
<h2>Free Legal Help Near {name}</h2>
<div class="card">
<ul>
<li><strong>Atlanta Legal Aid Society</strong> -- Free legal services for low-income residents of metro Atlanta, including {county}.</li>
<li><strong>Georgia Legal Services Program</strong> -- Serves residents across Georgia.</li>
<li><strong>Atlanta Volunteer Lawyers Foundation</strong> -- Connects low-income residents with volunteer attorneys.</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>Where do I file bankruptcy if I live in {name}?</summary><div class="answer"><p>{name} is in {county}, part of the Northern District of Georgia. You file at 75 Ted Turner Dr SW, Atlanta, GA 30303. <a href="/atlanta/">Atlanta bankruptcy guide</a>.</p></div></details>
<details class="faq-item"><summary>How much does bankruptcy cost in {name}?</summary><div class="answer"><p>Filing fees are $338 (Ch. 7) or $313 (Ch. 13). Attorney fees in the Atlanta area range from $1,200-$2,500 for Chapter 7 and $3,500-$5,000 for Chapter 13. <a href="/atlanta/cost.html">Full cost guide</a>.</p></div></details>
<details class="faq-item"><summary>What is the Chapter 13 dismissal rate?</summary><div class="answer"><p>The N.D. Ga. has a 72.9% Chapter 13 dismissal rate -- one of the worst in the nation. Choose your attorney carefully and consider Chapter 7 if you qualify.</p></div></details>
</div></section>

<div class="container">
<div class="card">
<h3>Other Atlanta-Area Guides</h3>
<div class="network-links" style="margin-top:8px">
<a href="/atlanta/">Atlanta</a>
{"".join(f'<a href="/atlanta/suburbs/{s}.html">{n}</a>' for s,n,_,_ in suburbs if s != slug)}
</div>
</div>
</div>"""
    )
    if write_if_missing(f"atlanta/suburbs/{slug}.html", html): created += 1


# ============================================================
# SAVANNAH - 5 pages
# ============================================================

# savannah/index
html = page(
    "Filing Bankruptcy in Savannah, Georgia -- 2026 Guide | Georgia Bankruptcy",
    "Free guide to filing bankruptcy in Savannah, GA. Southern District of Georgia courthouse, Chapter 7, Chapter 13, Georgia exemptions, and costs.",
    "https://georgiabankruptcy.org/savannah/",
    SAV_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Savannah","https://georgiabankruptcy.org/savannah/")],
    [("Where do I file bankruptcy in Savannah?","Savannah residents file in the Southern District of Georgia (S.D. Ga.) at the U.S. Bankruptcy Court, 125 Bull St, Savannah, GA 31401. Phone: (912) 650-4100."),
     ("How much does bankruptcy cost in Savannah?","Chapter 7 filing fees are $338 and Chapter 13 filing fees are $313. Attorney fees in Savannah typically range from $1,000 to $2,000 for Chapter 7 and $3,000 to $4,500 for Chapter 13."),
     ("What exemptions are available in Savannah?","Savannah filers use Georgia state exemptions: $21,500 homestead, $5,000 vehicle, $600+$5,000 wildcard. Retirement accounts and Social Security are fully exempt. Federal exemptions are not available in Georgia."),
     ("Should I file Chapter 7 or Chapter 13?","Chapter 7 eliminates most unsecured debt in 3-4 months but requires passing a means test. Chapter 13 allows you to keep property and catch up on missed payments over 3-5 years. Your income and goals determine the best choice."),
     ("Can I keep my home if I file in Savannah?","Yes, if your equity is within the $21,500 homestead exemption ($43,000 for joint filers). Chapter 13 can also stop foreclosure and let you catch up on missed mortgage payments over 3-5 years.")],
    """<div class="hero"><div class="container">
<h1>Filing Bankruptcy in Savannah, Georgia</h1>
<p class="subtitle">Savannah residents file bankruptcy in the Southern District of Georgia. This free guide covers Chapter 7, Chapter 13, Georgia exemptions, and what to expect at the Savannah courthouse.</p>
</div></div>

<div class="container">
<div class="stats-row">
<div class="stat-card"><div class="number">$21,500</div><div class="label">Homestead Exemption</div></div>
<div class="stat-card"><div class="number">$5,000</div><div class="label">Vehicle Exemption</div></div>
<div class="stat-card"><div class="number">$338</div><div class="label">Ch. 7 Filing Fee</div></div>
<div class="stat-card"><div class="number">$313</div><div class="label">Ch. 13 Filing Fee</div></div>
</div>
</div>

<section><div class="container">
<h2>Southern District of Georgia Courthouse</h2>
<div class="district-card">
<h3>U.S. Bankruptcy Court, S.D. Ga.</h3>
<p style="margin-top:12px"><strong>Address:</strong> 125 Bull St, Savannah, GA 31401</p>
<p><strong>Phone:</strong> (912) 650-4100</p>
<p><strong>Website:</strong> <a href="https://www.gasb.uscourts.gov" target="_blank" rel="noopener">gasb.uscourts.gov</a></p>
<div class="meta">The Southern District covers the coastal and southeastern counties of Georgia including Chatham County (Savannah), with additional divisional offices in Augusta, Brunswick, Dublin, and Statesboro.</div>
</div>
</div></section>

<section><div class="container">
<h2>Chapter 7 vs. Chapter 13 in Savannah</h2>
<div class="card">
<h3>Chapter 7 -- Fresh Start</h3>
<p>Chapter 7 eliminates most unsecured debts in about 3-4 months. You must pass a <a href="https://meanstest.org" target="_blank" rel="noopener">means test</a>.</p>
<ul>
<li>Discharge in 3-4 months</li>
<li>Eliminates credit cards, medical bills, personal loans</li>
<li>Filing fee: $338</li>
<li>Must pass the means test</li>
</ul>
<p><a href="/savannah/chapter-7.html">Savannah Chapter 7 guide &rarr;</a></p>
</div>
<div class="card">
<h3>Chapter 13 -- Payment Plan</h3>
<p>Chapter 13 lets you keep property while repaying debts over 3-5 years. Ideal for homeowners behind on mortgage payments.</p>
<ul>
<li>3-5 year repayment plan</li>
<li>Keep your home and car</li>
<li>Catch up on missed payments</li>
<li>Filing fee: $313</li>
</ul>
<p><a href="/savannah/chapter-13.html">Savannah Chapter 13 guide &rarr;</a></p>
</div>
</div></section>

<section><div class="container">
<h2>Georgia Exemptions for Savannah Filers</h2>
<div class="card">
<table>
<tr><th>Property</th><th>Georgia Exemption</th></tr>
<tr><td>Homestead (primary residence)</td><td>$21,500 ($43,000 married filing jointly)</td></tr>
<tr><td>Vehicle</td><td>$5,000</td></tr>
<tr><td>Personal property</td><td>$600 per item, $5,000 aggregate</td></tr>
<tr><td>Wildcard</td><td>$600 + up to $5,000 of unused homestead</td></tr>
<tr><td>Retirement accounts (401k/IRA)</td><td>Fully exempt</td></tr>
<tr><td>Social Security</td><td>Fully exempt</td></tr>
<tr><td>Workers' compensation</td><td>Fully exempt</td></tr>
</table>
<p style="margin-top:12px">Georgia does not allow filers to use federal exemptions. <a href="/savannah/exemptions.html">Full exemptions guide &rarr;</a></p>
</div>
</div></section>

<section><div class="container">
<h2>Cost of Filing in Savannah</h2>
<div class="card">
<ul>
<li><strong>Chapter 7 filing fee:</strong> $338</li>
<li><strong>Chapter 13 filing fee:</strong> $313</li>
<li><strong>Attorney fees:</strong> $1,000 to $2,000 for Chapter 7; $3,000 to $4,500 for Chapter 13</li>
<li><strong>Credit counseling courses:</strong> $25-50 total (two required)</li>
</ul>
<p>Fee waivers are available for Chapter 7 filers below 150% of the federal poverty guidelines.</p>
</div>
</div></section>

<section><div class="container">
<h2>Non-Judicial Foreclosure in Georgia</h2>
<div class="card">
<p>Georgia is a <strong>non-judicial foreclosure state</strong>. Lenders can foreclose without going to court, and the process can move in as few as 60 days. Filing bankruptcy triggers the <a href="https://automaticstay.org">automatic stay</a>, which immediately halts foreclosure.</p>
<p>If you are facing foreclosure in the Savannah area, time is critical. Chapter 13 allows you to catch up on missed payments while keeping your home.</p>
</div>
</div></section>

<section><div class="container">
<h2>Free Legal Help in Savannah</h2>
<div class="card">
<ul>
<li><strong>Georgia Legal Services Program (Savannah office)</strong> -- Free legal services for low-income residents of southeastern Georgia. Covers bankruptcy, foreclosure defense, and consumer debt issues.</li>
<li><strong>Savannah Bar Association Lawyer Referral Service</strong> -- Can connect you with local bankruptcy attorneys, some offering reduced-fee consultations.</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>Where do I file bankruptcy in Savannah?</summary><div class="answer"><p>At the U.S. Bankruptcy Court, 125 Bull St, Savannah, GA 31401. Phone: (912) 650-4100.</p></div></details>
<details class="faq-item"><summary>How much does it cost?</summary><div class="answer"><p>Filing fees: $338 (Ch. 7) or $313 (Ch. 13). Attorney fees: $1,000-$2,000 for Ch. 7, $3,000-$4,500 for Ch. 13. Credit counseling: $25-50 total.</p></div></details>
<details class="faq-item"><summary>What exemptions are available?</summary><div class="answer"><p>Georgia exemptions: $21,500 homestead, $5,000 vehicle, $600+$5,000 wildcard. Retirement and Social Security are fully exempt. <a href="/savannah/exemptions.html">Full guide</a>.</p></div></details>
<details class="faq-item"><summary>Should I file Chapter 7 or 13?</summary><div class="answer"><p>Chapter 7 is faster (3-4 months) and eliminates unsecured debt. Chapter 13 lets you keep property and catch up on payments over 3-5 years. Income and goals determine the best choice.</p></div></details>
<details class="faq-item"><summary>Can I keep my home?</summary><div class="answer"><p>Yes, if your equity is within the $21,500 exemption. Chapter 13 can stop foreclosure and let you catch up.</p></div></details>
</div></section>

<div class="container">
<div class="card">
<h3>Other Georgia City Guides</h3>
<div class="network-links" style="margin-top:8px">
<a href="/atlanta/">Atlanta</a>
<a href="/macon/">Macon</a>
</div>
</div>
</div>"""
)
if write_if_missing("savannah/index.html", html): created += 1

# savannah/chapter-7
html = page(
    "Chapter 7 Bankruptcy in Savannah, GA -- 2026 Guide | Georgia Bankruptcy",
    "Complete guide to Chapter 7 bankruptcy in Savannah. Means test, Georgia exemptions, S.D. Ga. courthouse procedures, timeline, and what debts are eliminated.",
    "https://georgiabankruptcy.org/savannah/chapter-7.html",
    SAV_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Savannah","https://georgiabankruptcy.org/savannah/"),("Chapter 7","https://georgiabankruptcy.org/savannah/chapter-7.html")],
    [("Do I qualify for Chapter 7 in Savannah?","You must pass the means test. If your household income is below Georgia's median (approximately $55,000 for a single filer), you automatically qualify. If above, you may still qualify after deducting allowed expenses."),
     ("What debts does Chapter 7 eliminate?","Chapter 7 eliminates most unsecured debts including credit cards, medical bills, personal loans, and utility arrears. It does not eliminate student loans (except in rare cases), recent taxes, child support, or alimony."),
     ("How long does Chapter 7 take in Savannah?","Most Chapter 7 cases in the Southern District take 3-4 months from filing to discharge.")],
    """<div class="hero"><div class="container">
<h1>Chapter 7 Bankruptcy in Savannah, Georgia</h1>
<p class="subtitle">Chapter 7 is the fastest path to debt relief for Savannah residents. Most filers receive a discharge in 3-4 months, eliminating credit card debt, medical bills, and other unsecured obligations.</p>
</div></div>

<section><div class="container">
<h2>How Chapter 7 Works</h2>
<div class="card">
<p>Chapter 7 bankruptcy (sometimes called "liquidation bankruptcy") eliminates most unsecured debts. A court-appointed trustee reviews your assets to determine if any non-exempt property can be sold to pay creditors. In practice, most Chapter 7 cases are "no-asset" cases where the filer keeps everything.</p>
<ol>
<li>Complete credit counseling course</li>
<li>File petition with the S.D. Ga. at 125 Bull St, Savannah</li>
<li>Automatic stay stops all collection activity</li>
<li>Attend <a href="https://341meeting.org">341 meeting</a> (~30 days after filing)</li>
<li>Complete debtor education course</li>
<li>Receive discharge (~90 days after filing)</li>
</ol>
</div>
</div></section>

<section><div class="container">
<h2>The Means Test for Savannah Filers</h2>
<div class="card">
<p>The <a href="https://meanstest.org" target="_blank" rel="noopener">means test</a> compares your household income to Georgia's median. If below, you qualify automatically.</p>
<table>
<tr><th>Household Size</th><th>Georgia Median (approx.)</th></tr>
<tr><td>1 person</td><td>$55,234</td></tr>
<tr><td>2 people</td><td>$72,108</td></tr>
<tr><td>3 people</td><td>$82,563</td></tr>
<tr><td>4 people</td><td>$98,725</td></tr>
</table>
<p style="margin-top:12px">If above the median, you may still qualify after deducting allowed expenses. If you do not qualify, <a href="/savannah/chapter-13.html">Chapter 13</a> is available with no income limit.</p>
</div>
</div></section>

<section><div class="container">
<h2>What Debts Are Eliminated</h2>
<div class="card">
<h3>Dischargeable (eliminated)</h3>
<ul>
<li>Credit card balances</li>
<li>Medical bills</li>
<li>Personal loans and payday loans</li>
<li>Utility arrears</li>
<li>Old lease obligations</li>
<li>Deficiency balances after repossession or foreclosure</li>
</ul>
<h3>Not dischargeable</h3>
<ul>
<li>Student loans (except in rare hardship cases)</li>
<li>Recent income taxes (generally last 3 years)</li>
<li>Child support and alimony</li>
<li>Court fines and restitution</li>
<li>Debts from fraud or willful injury</li>
<li>DUI-related judgments</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>Georgia Exemptions</h2>
<div class="card">
<p>Georgia does not allow federal exemptions. Savannah filers must use state exemptions:</p>
<table>
<tr><th>Property</th><th>Exemption</th></tr>
<tr><td>Homestead</td><td>$21,500 ($43,000 joint)</td></tr>
<tr><td>Vehicle</td><td>$5,000</td></tr>
<tr><td>Personal property</td><td>$600/item, $5,000 total</td></tr>
<tr><td>Wildcard</td><td>$600 + up to $5,000 unused homestead</td></tr>
<tr><td>Retirement (401k/IRA)</td><td>Fully exempt</td></tr>
</table>
<p style="margin-top:12px"><a href="/savannah/exemptions.html">Full exemptions guide</a></p>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>Do I qualify for Chapter 7 in Savannah?</summary><div class="answer"><p>If your income is below Georgia's median (~$55,000 for a single filer), you qualify automatically. If above, you may still qualify after deductions.</p></div></details>
<details class="faq-item"><summary>What debts does Chapter 7 eliminate?</summary><div class="answer"><p>Credit cards, medical bills, personal loans, utility arrears, and most other unsecured debts. Not student loans, recent taxes, or support obligations.</p></div></details>
<details class="faq-item"><summary>How long does it take?</summary><div class="answer"><p>3-4 months from filing to discharge in the S.D. Ga.</p></div></details>
</div></section>"""
)
if write_if_missing("savannah/chapter-7.html", html): created += 1

# savannah/chapter-13
html = page(
    "Chapter 13 Bankruptcy in Savannah, GA -- 2026 Guide | Georgia Bankruptcy",
    "Guide to Chapter 13 bankruptcy in Savannah. Repayment plans, keeping your home, the automatic stay, and filing in the Southern District of Georgia.",
    "https://georgiabankruptcy.org/savannah/chapter-13.html",
    SAV_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Savannah","https://georgiabankruptcy.org/savannah/"),("Chapter 13","https://georgiabankruptcy.org/savannah/chapter-13.html")],
    [("How does Chapter 13 work in Savannah?","Chapter 13 lets you keep your property while repaying debts over 3-5 years through a court-approved plan. You make monthly payments to a Chapter 13 trustee who distributes them to creditors. Remaining unsecured debt is discharged at completion."),
     ("Can Chapter 13 stop foreclosure?","Yes. Filing Chapter 13 triggers the automatic stay, which immediately stops foreclosure. Your plan allows you to catch up on missed mortgage payments over 3-5 years while making current payments going forward."),
     ("How much are Chapter 13 payments?","Payments are based on your disposable income -- the difference between what you earn and what you need for reasonable living expenses. The trustee and court review your budget to determine a fair amount.")],
    """<div class="hero"><div class="container">
<h1>Chapter 13 Bankruptcy in Savannah, Georgia</h1>
<p class="subtitle">Chapter 13 lets you keep your property while repaying debts over 3-5 years. It is the primary tool for Savannah homeowners facing foreclosure or anyone who does not qualify for Chapter 7.</p>
</div></div>

<section><div class="container">
<h2>How Chapter 13 Works</h2>
<div class="card">
<p>Chapter 13 is a reorganization plan. You propose a 3-5 year repayment plan to the court, and if approved, you make monthly payments to a Chapter 13 trustee who distributes them to your creditors.</p>
<ol>
<li>Complete credit counseling</li>
<li>File petition and proposed plan with S.D. Ga.</li>
<li>Automatic stay stops all collection activity</li>
<li>First payment due within 30 days</li>
<li>341 meeting (~30 days after filing)</li>
<li>Plan confirmation hearing (2-4 months)</li>
<li>Make plan payments for 3-5 years</li>
<li>Complete debtor education course</li>
<li>Receive discharge</li>
</ol>
</div>
</div></section>

<section><div class="container">
<h2>What Chapter 13 Can Do</h2>
<div class="card">
<ul>
<li><strong>Stop foreclosure</strong> and cure mortgage arrears over 3-5 years</li>
<li><strong>Stop repossession</strong> and catch up on car payments</li>
<li><strong>Cramdown car loans</strong> to the vehicle's current value (if purchased 910+ days before filing)</li>
<li><strong>Strip second mortgages</strong> if your home is underwater</li>
<li><strong>Catch up on tax debt</strong> through the plan</li>
<li><strong>Protect co-signers</strong> from collection through the co-debtor stay</li>
<li><strong>Eliminate remaining unsecured debt</strong> after plan completion</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>Plan Length: 3 Years or 5 Years?</h2>
<div class="card">
<p>Your plan length depends on your income relative to Georgia's median:</p>
<ul>
<li><strong>Below median income:</strong> 3-year plan (can extend to 5 years with court approval)</li>
<li><strong>Above median income:</strong> 5-year plan required</li>
</ul>
<p>During the plan, you must commit all disposable income to the plan payments. The court determines what counts as reasonable living expenses.</p>
</div>
</div></section>

<section><div class="container">
<h2>Filing at the Savannah Courthouse</h2>
<div class="card">
<p><strong>Address:</strong> 125 Bull St, Savannah, GA 31401</p>
<p><strong>Phone:</strong> (912) 650-4100</p>
<p><strong>Website:</strong> <a href="https://www.gasb.uscourts.gov" target="_blank" rel="noopener">gasb.uscourts.gov</a></p>
<p>The Chapter 13 trustee for the Southern District will review your plan and may negotiate adjustments before the confirmation hearing.</p>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>How does Chapter 13 work?</summary><div class="answer"><p>You propose a 3-5 year repayment plan. A trustee distributes your monthly payments to creditors. Remaining unsecured debt is discharged at plan completion.</p></div></details>
<details class="faq-item"><summary>Can Chapter 13 stop foreclosure?</summary><div class="answer"><p>Yes. The automatic stay halts foreclosure immediately, and your plan allows you to cure missed payments over 3-5 years. <a href="https://automaticstay.org">Automatic stay guide</a>.</p></div></details>
<details class="faq-item"><summary>How much are payments?</summary><div class="answer"><p>Based on your disposable income. The court reviews your budget to determine a fair monthly amount.</p></div></details>
</div></section>"""
)
if write_if_missing("savannah/chapter-13.html", html): created += 1

# savannah/exemptions
html = page(
    "Georgia Bankruptcy Exemptions in Savannah -- 2026 Guide | Georgia Bankruptcy",
    "Complete guide to Georgia bankruptcy exemptions for Savannah filers. Homestead ($21,500), vehicle ($5,000), wildcard, retirement, and personal property exemptions.",
    "https://georgiabankruptcy.org/savannah/exemptions.html",
    SAV_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Savannah","https://georgiabankruptcy.org/savannah/"),("Exemptions","https://georgiabankruptcy.org/savannah/exemptions.html")],
    [("What are Georgia's bankruptcy exemptions?","Georgia exemptions protect specific property in bankruptcy: $21,500 homestead, $5,000 vehicle, $600 per item personal property ($5,000 total), $600+$5,000 wildcard, plus full exemptions for retirement accounts and Social Security."),
     ("Can I use federal exemptions in Georgia?","No. Georgia is one of the states that does not allow filers to choose federal exemptions. You must use Georgia's state exemptions."),
     ("What is the wildcard exemption?","The wildcard exemption is $600 plus up to $5,000 of any unused portion of your homestead exemption. It can be applied to any property, including cash, bank accounts, or vehicle equity beyond the $5,000 vehicle exemption.")],
    """<div class="hero"><div class="container">
<h1>Georgia Bankruptcy Exemptions for Savannah Filers</h1>
<p class="subtitle">Exemptions determine what property you can keep when filing bankruptcy. Georgia does not allow federal exemptions -- you must use state exemptions listed here.</p>
</div></div>

<section><div class="container">
<h2>Georgia Exemptions at a Glance</h2>
<div class="card">
<table>
<tr><th>Property</th><th>Exemption</th><th>Statute</th></tr>
<tr><td>Homestead (primary residence)</td><td>$21,500 ($43,000 married filing jointly)</td><td>O.C.G.A. 44-13-100(a)(1)</td></tr>
<tr><td>Motor vehicle</td><td>$5,000</td><td>O.C.G.A. 44-13-100(a)(3)</td></tr>
<tr><td>Household goods &amp; furnishings</td><td>$600 per item, $5,000 aggregate</td><td>O.C.G.A. 44-13-100(a)(4)</td></tr>
<tr><td>Jewelry</td><td>$500</td><td>O.C.G.A. 44-13-100(a)(5)</td></tr>
<tr><td>Tools of the trade</td><td>$1,500</td><td>O.C.G.A. 44-13-100(a)(7)</td></tr>
<tr><td>Wildcard</td><td>$600 + up to $5,000 of unused homestead</td><td>O.C.G.A. 44-13-100(a)(6)</td></tr>
<tr><td>Health aids</td><td>Unlimited</td><td>O.C.G.A. 44-13-100(a)(9)</td></tr>
<tr><td>Retirement accounts (401k/IRA)</td><td>Fully exempt</td><td>O.C.G.A. 44-13-100(a)(2.1)</td></tr>
<tr><td>Social Security benefits</td><td>Fully exempt</td><td>42 U.S.C. 407</td></tr>
<tr><td>Workers' compensation</td><td>Fully exempt</td><td>O.C.G.A. 34-9-84</td></tr>
<tr><td>Unemployment compensation</td><td>Fully exempt</td><td>O.C.G.A. 34-8-253</td></tr>
<tr><td>Public assistance</td><td>Fully exempt</td><td>O.C.G.A. 49-4-35</td></tr>
<tr><td>Alimony/child support</td><td>As needed for support</td><td>O.C.G.A. 44-13-100(a)(2)(D)</td></tr>
</table>
</div>
</div></section>

<section><div class="container">
<h2>Understanding the Wildcard Exemption</h2>
<div class="card">
<p>Georgia's wildcard exemption is $600 plus up to $5,000 of any unused homestead exemption. This means:</p>
<ul>
<li><strong>If you do not own a home:</strong> You get $600 + $5,000 = $5,600 wildcard to apply to any property</li>
<li><strong>If you own a home and use all $21,500 of homestead:</strong> You get only $600 wildcard</li>
<li><strong>If you own a home with $16,500 equity (using only $16,500 of homestead):</strong> You get $600 + $5,000 = $5,600 wildcard</li>
</ul>
<p>The wildcard can be applied to anything: cash, bank accounts, tax refunds, extra vehicle equity, or any other property.</p>
</div>
</div></section>

<section><div class="container">
<h2>No Federal Exemptions in Georgia</h2>
<div class="card">
<p>Georgia is one of the states that <strong>opts out</strong> of the federal bankruptcy exemption system under 11 U.S.C. section 522(b). You must use Georgia's state exemptions -- you cannot choose federal exemptions instead.</p>
<p>This is important because federal exemptions have different amounts (for example, a higher homestead in some cases). But Georgia law controls for Savannah filers.</p>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>What are Georgia's exemptions?</summary><div class="answer"><p>$21,500 homestead, $5,000 vehicle, $600/item personal property ($5,000 total), $600+$5,000 wildcard, and full exemptions for retirement accounts and Social Security.</p></div></details>
<details class="faq-item"><summary>Can I use federal exemptions?</summary><div class="answer"><p>No. Georgia does not allow filers to choose federal exemptions. You must use Georgia state exemptions.</p></div></details>
<details class="faq-item"><summary>What is the wildcard?</summary><div class="answer"><p>$600 plus up to $5,000 of unused homestead exemption, applicable to any property. If you do not own a home, you get the full $5,600 wildcard.</p></div></details>
</div></section>"""
)
if write_if_missing("savannah/exemptions.html", html): created += 1

# savannah/faq
html = page(
    "Savannah Bankruptcy FAQ -- Common Questions Answered | Georgia Bankruptcy",
    "Answers to common bankruptcy questions for Savannah, Georgia residents. Chapter 7, Chapter 13, exemptions, costs, timeline, and the S.D. Ga. courthouse.",
    "https://georgiabankruptcy.org/savannah/faq.html",
    SAV_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Savannah","https://georgiabankruptcy.org/savannah/"),("FAQ","https://georgiabankruptcy.org/savannah/faq.html")],
    [("How much does bankruptcy cost in Savannah?","Chapter 7 filing fees are $338 and Chapter 13 filing fees are $313. Attorney fees in Savannah typically range from $1,000 to $2,000 for Chapter 7 and $3,000 to $4,500 for Chapter 13."),
     ("Will I lose my house?","Georgia's homestead exemption protects up to $21,500 of equity ($43,000 for joint filers). If your equity is within these limits, you keep your home. Chapter 13 can stop foreclosure."),
     ("How long does bankruptcy take?","Chapter 7: 3-4 months. Chapter 13: 3-5 years. The 341 meeting happens about 30 days after filing."),
     ("Will bankruptcy stop wage garnishment?","Yes. The automatic stay stops wage garnishment the moment your case is filed. Your employer must be notified of the filing."),
     ("Can I file bankruptcy without an attorney?","Yes, you can file pro se (without an attorney). However, bankruptcy is complex and mistakes can cost you property or result in dismissal. Most people benefit from professional help."),
     ("What happens to my credit score?","Bankruptcy stays on your credit report for 7 years (Chapter 13) or 10 years (Chapter 7). Most filers see improvement within 1-2 years as they rebuild."),
     ("Can I file bankruptcy on student loans?","Student loans are generally not dischargeable except in rare cases of undue hardship. You must file a separate adversary proceeding and prove you cannot maintain a minimal standard of living."),
     ("How often can I file bankruptcy?","Chapter 7 to Chapter 7: 8 years. Chapter 13 to Chapter 13: 2 years. Chapter 7 to Chapter 13: 4 years. Chapter 13 to Chapter 7: 6 years. Check eligibility at 1328f.com.")],
    """<div class="hero"><div class="container">
<h1>Savannah Bankruptcy FAQ</h1>
<p class="subtitle">Answers to the most common questions about filing bankruptcy in Savannah and the Southern District of Georgia.</p>
</div></div>

<section><div class="container">
<h2>Frequently Asked Questions</h2>

<details class="faq-item"><summary>How much does bankruptcy cost in Savannah?</summary><div class="answer"><p>Chapter 7 filing fees are $338 and Chapter 13 fees are $313. Attorney fees typically range from $1,000-$2,000 for Chapter 7 and $3,000-$4,500 for Chapter 13 in the Savannah area. Two credit counseling courses cost $25-50 total. Fee waivers available for Chapter 7 filers below 150% of poverty. <a href="https://howmuchdoesbankruptcycost.com" target="_blank" rel="noopener">National cost guide</a>.</p></div></details>

<details class="faq-item"><summary>Will I lose my house?</summary><div class="answer"><p>Georgia's homestead exemption protects up to $21,500 of equity ($43,000 for joint filers). If your equity is within that amount, you keep your home in Chapter 7. Chapter 13 can stop foreclosure and let you catch up on missed payments. <a href="/savannah/exemptions.html">Full exemptions guide</a>.</p></div></details>

<details class="faq-item"><summary>How long does bankruptcy take?</summary><div class="answer"><p>Chapter 7: 3-4 months from filing to discharge. Chapter 13: 3-5 year repayment plan. The 341 meeting of creditors is about 30 days after filing. <a href="https://341meeting.org" target="_blank" rel="noopener">341 meeting guide</a>.</p></div></details>

<details class="faq-item"><summary>Will bankruptcy stop wage garnishment?</summary><div class="answer"><p>Yes. The <a href="https://automaticstay.org" target="_blank" rel="noopener">automatic stay</a> halts wage garnishment the moment your case is filed. Notify your employer and the garnishing creditor of the filing.</p></div></details>

<details class="faq-item"><summary>Can I file bankruptcy without an attorney?</summary><div class="answer"><p>Yes (called "pro se" filing), but it is not recommended. Bankruptcy law is complex and errors can result in loss of property, denial of discharge, or dismissal. The Southern District of Georgia has a pro se clinic for guidance.</p></div></details>

<details class="faq-item"><summary>What happens to my credit score?</summary><div class="answer"><p>Bankruptcy stays on your credit report for 7 years (Chapter 13) or 10 years (Chapter 7). The impact decreases over time. Most filers see significant improvement within 1-2 years. <a href="https://rebuildcreditafterbankruptcy.com" target="_blank" rel="noopener">Credit rebuilding guide</a>.</p></div></details>

<details class="faq-item"><summary>Can I discharge student loans?</summary><div class="answer"><p>Generally no, unless you can prove "undue hardship" through a separate adversary proceeding. This is a high standard, but not impossible. Consult an attorney about your specific situation.</p></div></details>

<details class="faq-item"><summary>How often can I file bankruptcy?</summary><div class="answer"><p>Waiting periods between filings: Ch. 7 to Ch. 7: 8 years. Ch. 13 to Ch. 13: 2 years. Ch. 7 to Ch. 13: 4 years. Ch. 13 to Ch. 7: 6 years. <a href="https://1328f.com" target="_blank" rel="noopener">Check your eligibility</a>. <a href="https://filebankruptcyagain.com" target="_blank" rel="noopener">Filing again guide</a>.</p></div></details>

<details class="faq-item"><summary>Where do I file in Savannah?</summary><div class="answer"><p>U.S. Bankruptcy Court, Southern District of Georgia, 125 Bull St, Savannah, GA 31401. Phone: (912) 650-4100. Website: <a href="https://www.gasb.uscourts.gov" target="_blank" rel="noopener">gasb.uscourts.gov</a>.</p></div></details>

<details class="faq-item"><summary>Can I keep my car?</summary><div class="answer"><p>Georgia's vehicle exemption protects up to $5,000 of equity. If you owe more than the car is worth, you have no equity to protect. The wildcard ($600 + up to $5,000 unused homestead) can cover additional equity. <a href="https://keepmycarinbankruptcy.com" target="_blank" rel="noopener">Full car guide</a>.</p></div></details>
</div></section>"""
)
if write_if_missing("savannah/faq.html", html): created += 1


# ============================================================
# MACON - 5 pages
# ============================================================

# macon/index
html = page(
    "Filing Bankruptcy in Macon, Georgia -- 2026 Guide | Georgia Bankruptcy",
    "Free guide to filing bankruptcy in Macon, GA. Middle District of Georgia courthouse, Chapter 7, Chapter 13, Georgia exemptions, and costs.",
    "https://georgiabankruptcy.org/macon/",
    MAC_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Macon","https://georgiabankruptcy.org/macon/")],
    [("Where do I file bankruptcy in Macon?","Macon residents file in the Middle District of Georgia (M.D. Ga.) at the U.S. Bankruptcy Court, 475 Mulberry St, Macon, GA 31201. Phone: (478) 752-3506."),
     ("How much does bankruptcy cost in Macon?","Chapter 7 filing fees are $338 and Chapter 13 filing fees are $313. Attorney fees in Macon typically range from $1,000 to $1,800 for Chapter 7 and $2,500 to $4,000 for Chapter 13."),
     ("What exemptions are available?","Georgia exemptions: $21,500 homestead, $5,000 vehicle, $600+$5,000 wildcard. Retirement and Social Security are fully exempt. Federal exemptions are not available in Georgia."),
     ("Should I file Chapter 7 or Chapter 13?","Chapter 7 eliminates most unsecured debt in 3-4 months but requires passing a means test. Chapter 13 allows you to keep property and repay debts over 3-5 years."),
     ("Can I keep my home filing in Macon?","Yes, if your equity is within the $21,500 homestead exemption. Chapter 13 can stop foreclosure and let you catch up on missed payments.")],
    """<div class="hero"><div class="container">
<h1>Filing Bankruptcy in Macon, Georgia</h1>
<p class="subtitle">Macon residents file bankruptcy in the Middle District of Georgia. This free guide covers Chapter 7, Chapter 13, Georgia exemptions, and what to expect at the Macon courthouse.</p>
</div></div>

<div class="container">
<div class="stats-row">
<div class="stat-card"><div class="number">$21,500</div><div class="label">Homestead Exemption</div></div>
<div class="stat-card"><div class="number">$5,000</div><div class="label">Vehicle Exemption</div></div>
<div class="stat-card"><div class="number">$338</div><div class="label">Ch. 7 Filing Fee</div></div>
<div class="stat-card"><div class="number">$313</div><div class="label">Ch. 13 Filing Fee</div></div>
</div>
</div>

<section><div class="container">
<h2>Middle District of Georgia Courthouse</h2>
<div class="district-card">
<h3>U.S. Bankruptcy Court, M.D. Ga.</h3>
<p style="margin-top:12px"><strong>Address:</strong> 475 Mulberry St, Macon, GA 31201</p>
<p><strong>Phone:</strong> (478) 752-3506</p>
<p><strong>Website:</strong> <a href="https://www.gamb.uscourts.gov" target="_blank" rel="noopener">gamb.uscourts.gov</a></p>
<div class="meta">The Middle District covers central Georgia counties including Bibb (Macon), Houston (Warner Robins), Baldwin (Milledgeville), Laurens (Dublin), Muscogee (Columbus), and Dougherty (Albany), with divisional offices in several cities.</div>
</div>
</div></section>

<section><div class="container">
<h2>Chapter 7 vs. Chapter 13 in Macon</h2>
<div class="card">
<h3>Chapter 7 -- Fresh Start</h3>
<p>Chapter 7 eliminates most unsecured debts in about 3-4 months. You must pass a <a href="https://meanstest.org" target="_blank" rel="noopener">means test</a>.</p>
<ul>
<li>Discharge in 3-4 months</li>
<li>Eliminates credit cards, medical bills, personal loans</li>
<li>Filing fee: $338</li>
<li>Must pass the means test</li>
</ul>
<p><a href="/macon/chapter-7.html">Macon Chapter 7 guide &rarr;</a></p>
</div>
<div class="card">
<h3>Chapter 13 -- Payment Plan</h3>
<p>Chapter 13 lets you keep property while repaying debts over 3-5 years. Ideal for homeowners facing foreclosure.</p>
<ul>
<li>3-5 year repayment plan</li>
<li>Keep your home and car</li>
<li>Catch up on missed payments</li>
<li>Filing fee: $313</li>
</ul>
<p><a href="/macon/chapter-13.html">Macon Chapter 13 guide &rarr;</a></p>
</div>
</div></section>

<section><div class="container">
<h2>Georgia Exemptions for Macon Filers</h2>
<div class="card">
<table>
<tr><th>Property</th><th>Georgia Exemption</th></tr>
<tr><td>Homestead (primary residence)</td><td>$21,500 ($43,000 married filing jointly)</td></tr>
<tr><td>Vehicle</td><td>$5,000</td></tr>
<tr><td>Personal property</td><td>$600 per item, $5,000 aggregate</td></tr>
<tr><td>Wildcard</td><td>$600 + up to $5,000 of unused homestead</td></tr>
<tr><td>Retirement accounts (401k/IRA)</td><td>Fully exempt</td></tr>
<tr><td>Social Security</td><td>Fully exempt</td></tr>
<tr><td>Workers' compensation</td><td>Fully exempt</td></tr>
</table>
<p style="margin-top:12px">Georgia does not allow federal exemptions. <a href="/macon/exemptions.html">Full exemptions guide &rarr;</a></p>
</div>
</div></section>

<section><div class="container">
<h2>Cost of Filing in Macon</h2>
<div class="card">
<ul>
<li><strong>Chapter 7 filing fee:</strong> $338</li>
<li><strong>Chapter 13 filing fee:</strong> $313</li>
<li><strong>Attorney fees:</strong> $1,000 to $1,800 for Chapter 7; $2,500 to $4,000 for Chapter 13</li>
<li><strong>Credit counseling courses:</strong> $25-50 total (two required)</li>
</ul>
<p>Attorney fees in central Georgia are generally lower than in metro Atlanta. Fee waivers are available for Chapter 7 filers below 150% of the poverty guidelines.</p>
</div>
</div></section>

<section><div class="container">
<h2>Non-Judicial Foreclosure in Georgia</h2>
<div class="card">
<p>Georgia is a <strong>non-judicial foreclosure state</strong>. Lenders can foreclose without court involvement, and the process can happen in as few as 60 days. Filing bankruptcy triggers the <a href="https://automaticstay.org">automatic stay</a>, which immediately halts foreclosure.</p>
<p>If you are behind on your mortgage in the Macon area, consult with a bankruptcy attorney before the foreclosure sale date.</p>
</div>
</div></section>

<section><div class="container">
<h2>Free Legal Help in Macon</h2>
<div class="card">
<ul>
<li><strong>Georgia Legal Services Program (Macon office)</strong> -- Free legal services for low-income residents of central Georgia, including bankruptcy, foreclosure defense, and consumer debt.</li>
<li><strong>Macon Bar Association</strong> -- Lawyer referral service that can connect you with local bankruptcy attorneys.</li>
<li><strong>Mercer University School of Law Legal Clinic</strong> -- May provide free or low-cost legal assistance for qualifying individuals.</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>Where do I file bankruptcy in Macon?</summary><div class="answer"><p>U.S. Bankruptcy Court, 475 Mulberry St, Macon, GA 31201. Phone: (478) 752-3506.</p></div></details>
<details class="faq-item"><summary>How much does it cost?</summary><div class="answer"><p>Filing fees: $338 (Ch. 7) or $313 (Ch. 13). Attorney fees: $1,000-$1,800 for Ch. 7, $2,500-$4,000 for Ch. 13. Credit counseling: $25-50 total.</p></div></details>
<details class="faq-item"><summary>What exemptions are available?</summary><div class="answer"><p>Georgia state exemptions: $21,500 homestead, $5,000 vehicle, $600+$5,000 wildcard. Retirement and Social Security fully exempt. <a href="/macon/exemptions.html">Full guide</a>.</p></div></details>
<details class="faq-item"><summary>Chapter 7 or Chapter 13?</summary><div class="answer"><p>Chapter 7 eliminates debt in 3-4 months (means test required). Chapter 13 lets you keep property and repay over 3-5 years. <a href="https://chapter7vs13.org" target="_blank" rel="noopener">Compare chapters</a>.</p></div></details>
<details class="faq-item"><summary>Can I keep my home?</summary><div class="answer"><p>Yes, if equity is within the $21,500 exemption. Chapter 13 can stop foreclosure.</p></div></details>
</div></section>

<div class="container">
<div class="card">
<h3>Other Georgia City Guides</h3>
<div class="network-links" style="margin-top:8px">
<a href="/atlanta/">Atlanta</a>
<a href="/savannah/">Savannah</a>
</div>
</div>
</div>"""
)
if write_if_missing("macon/index.html", html): created += 1

# macon/chapter-7
html = page(
    "Chapter 7 Bankruptcy in Macon, GA -- 2026 Guide | Georgia Bankruptcy",
    "Complete guide to Chapter 7 bankruptcy in Macon. Means test, Georgia exemptions, M.D. Ga. courthouse procedures, timeline, and what debts are eliminated.",
    "https://georgiabankruptcy.org/macon/chapter-7.html",
    MAC_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Macon","https://georgiabankruptcy.org/macon/"),("Chapter 7","https://georgiabankruptcy.org/macon/chapter-7.html")],
    [("Do I qualify for Chapter 7 in Macon?","You must pass the means test. If your household income is below Georgia's median (approximately $55,000 for a single filer), you automatically qualify. If above, you may still qualify after deducting expenses."),
     ("What debts does Chapter 7 eliminate?","Credit cards, medical bills, personal loans, utility arrears, and most other unsecured debts. It does not eliminate student loans, recent taxes, child support, or alimony."),
     ("How long does Chapter 7 take in Macon?","Most Chapter 7 cases in the Middle District take 3-4 months from filing to discharge.")],
    """<div class="hero"><div class="container">
<h1>Chapter 7 Bankruptcy in Macon, Georgia</h1>
<p class="subtitle">Chapter 7 is the fastest path to debt relief for Macon residents. Most filers receive a discharge in 3-4 months, eliminating credit card debt, medical bills, and other unsecured obligations.</p>
</div></div>

<section><div class="container">
<h2>How Chapter 7 Works</h2>
<div class="card">
<p>Chapter 7 eliminates most unsecured debts. A trustee reviews your assets, but most cases are "no-asset" cases where filers keep everything that is exempt under Georgia law.</p>
<ol>
<li>Complete credit counseling course</li>
<li>File petition with M.D. Ga. at 475 Mulberry St, Macon</li>
<li>Automatic stay stops all collection activity</li>
<li>Attend <a href="https://341meeting.org">341 meeting</a> (~30 days after filing)</li>
<li>Complete debtor education course</li>
<li>Receive discharge (~90 days after filing)</li>
</ol>
</div>
</div></section>

<section><div class="container">
<h2>The Means Test for Macon Filers</h2>
<div class="card">
<p>The <a href="https://meanstest.org" target="_blank" rel="noopener">means test</a> compares your income to Georgia's median. If below, you qualify automatically.</p>
<table>
<tr><th>Household Size</th><th>Georgia Median (approx.)</th></tr>
<tr><td>1 person</td><td>$55,234</td></tr>
<tr><td>2 people</td><td>$72,108</td></tr>
<tr><td>3 people</td><td>$82,563</td></tr>
<tr><td>4 people</td><td>$98,725</td></tr>
</table>
<p style="margin-top:12px;color:#8b949e;font-size:0.9rem">If above the median, expense deductions may still qualify you. If you do not pass, <a href="/macon/chapter-13.html">Chapter 13</a> has no income limit.</p>
</div>
</div></section>

<section><div class="container">
<h2>What Debts Are Eliminated</h2>
<div class="card">
<h3>Dischargeable</h3>
<ul>
<li>Credit card balances</li>
<li>Medical bills</li>
<li>Personal loans and payday loans</li>
<li>Utility arrears</li>
<li>Deficiency balances after repossession or foreclosure</li>
</ul>
<h3>Not dischargeable</h3>
<ul>
<li>Student loans (except in rare hardship cases)</li>
<li>Recent income taxes (generally last 3 years)</li>
<li>Child support and alimony</li>
<li>Court fines and restitution</li>
<li>Debts from fraud or willful injury</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>Georgia Exemptions</h2>
<div class="card">
<table>
<tr><th>Property</th><th>Exemption</th></tr>
<tr><td>Homestead</td><td>$21,500 ($43,000 joint)</td></tr>
<tr><td>Vehicle</td><td>$5,000</td></tr>
<tr><td>Personal property</td><td>$600/item, $5,000 total</td></tr>
<tr><td>Wildcard</td><td>$600 + up to $5,000 unused homestead</td></tr>
<tr><td>Retirement (401k/IRA)</td><td>Fully exempt</td></tr>
</table>
<p style="margin-top:12px"><a href="/macon/exemptions.html">Full exemptions guide</a></p>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>Do I qualify for Chapter 7 in Macon?</summary><div class="answer"><p>If your income is below Georgia's median (~$55,000 for a single filer), you qualify automatically. If above, you may still qualify after deductions.</p></div></details>
<details class="faq-item"><summary>What debts does Chapter 7 eliminate?</summary><div class="answer"><p>Credit cards, medical bills, personal loans, and most other unsecured debts. Not student loans, recent taxes, or support obligations.</p></div></details>
<details class="faq-item"><summary>How long does it take?</summary><div class="answer"><p>3-4 months from filing to discharge in the M.D. Ga.</p></div></details>
</div></section>"""
)
if write_if_missing("macon/chapter-7.html", html): created += 1

# macon/chapter-13
html = page(
    "Chapter 13 Bankruptcy in Macon, GA -- 2026 Guide | Georgia Bankruptcy",
    "Guide to Chapter 13 bankruptcy in Macon. Repayment plans, keeping your home, the automatic stay, and filing in the Middle District of Georgia.",
    "https://georgiabankruptcy.org/macon/chapter-13.html",
    MAC_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Macon","https://georgiabankruptcy.org/macon/"),("Chapter 13","https://georgiabankruptcy.org/macon/chapter-13.html")],
    [("How does Chapter 13 work in Macon?","Chapter 13 lets you keep your property while repaying debts over 3-5 years through a court-approved plan. You make monthly payments to a trustee who distributes to creditors. Remaining unsecured debt is discharged at completion."),
     ("Can Chapter 13 stop foreclosure in Macon?","Yes. Filing triggers the automatic stay, immediately halting foreclosure. Your plan allows you to cure missed payments over 3-5 years."),
     ("How much are Chapter 13 payments?","Based on your disposable income -- the difference between your earnings and reasonable expenses. The court determines a fair amount.")],
    """<div class="hero"><div class="container">
<h1>Chapter 13 Bankruptcy in Macon, Georgia</h1>
<p class="subtitle">Chapter 13 lets Macon residents keep their property while repaying debts over 3-5 years. It is the primary tool for homeowners facing foreclosure or anyone who does not qualify for Chapter 7.</p>
</div></div>

<section><div class="container">
<h2>How Chapter 13 Works</h2>
<div class="card">
<ol>
<li>Complete credit counseling</li>
<li>File petition and plan with M.D. Ga. at 475 Mulberry St, Macon</li>
<li>Automatic stay stops all collection activity</li>
<li>First payment due within 30 days</li>
<li>341 meeting (~30 days after filing)</li>
<li>Plan confirmation hearing (2-4 months)</li>
<li>Make plan payments for 3-5 years</li>
<li>Complete debtor education course</li>
<li>Receive discharge</li>
</ol>
</div>
</div></section>

<section><div class="container">
<h2>What Chapter 13 Can Do</h2>
<div class="card">
<ul>
<li><strong>Stop foreclosure</strong> and cure mortgage arrears over 3-5 years</li>
<li><strong>Stop repossession</strong> and catch up on car payments</li>
<li><strong>Cramdown car loans</strong> to current value (if purchased 910+ days before filing)</li>
<li><strong>Strip underwater second mortgages</strong></li>
<li><strong>Catch up on tax debt</strong> through the plan</li>
<li><strong>Protect co-signers</strong> from collection</li>
<li><strong>Eliminate remaining unsecured debt</strong> at plan completion</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>Plan Length</h2>
<div class="card">
<ul>
<li><strong>Below Georgia median income:</strong> 3-year plan (extendable to 5 with court approval)</li>
<li><strong>Above Georgia median income:</strong> 5-year plan required</li>
</ul>
<p>All disposable income must go toward plan payments. The court determines reasonable living expenses.</p>
</div>
</div></section>

<section><div class="container">
<h2>Filing at the Macon Courthouse</h2>
<div class="card">
<p><strong>Address:</strong> 475 Mulberry St, Macon, GA 31201</p>
<p><strong>Phone:</strong> (478) 752-3506</p>
<p><strong>Website:</strong> <a href="https://www.gamb.uscourts.gov" target="_blank" rel="noopener">gamb.uscourts.gov</a></p>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>How does Chapter 13 work?</summary><div class="answer"><p>Propose a 3-5 year plan. A trustee distributes monthly payments to creditors. Remaining unsecured debt is discharged at completion.</p></div></details>
<details class="faq-item"><summary>Can it stop foreclosure?</summary><div class="answer"><p>Yes. The automatic stay halts foreclosure immediately. Your plan cures arrears over 3-5 years. <a href="https://automaticstay.org">Automatic stay guide</a>.</p></div></details>
<details class="faq-item"><summary>How much are payments?</summary><div class="answer"><p>Based on disposable income. The court reviews your budget to set a fair monthly amount.</p></div></details>
</div></section>"""
)
if write_if_missing("macon/chapter-13.html", html): created += 1

# macon/exemptions
html = page(
    "Georgia Bankruptcy Exemptions in Macon -- 2026 Guide | Georgia Bankruptcy",
    "Complete guide to Georgia bankruptcy exemptions for Macon filers. Homestead ($21,500), vehicle ($5,000), wildcard, retirement, and personal property exemptions.",
    "https://georgiabankruptcy.org/macon/exemptions.html",
    MAC_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Macon","https://georgiabankruptcy.org/macon/"),("Exemptions","https://georgiabankruptcy.org/macon/exemptions.html")],
    [("What are Georgia's bankruptcy exemptions?","Georgia exemptions protect specific property: $21,500 homestead, $5,000 vehicle, $600 per item personal property ($5,000 total), $600+$5,000 wildcard, plus full exemptions for retirement accounts and Social Security."),
     ("Can I use federal exemptions in Georgia?","No. Georgia opts out of federal exemptions. You must use Georgia state exemptions."),
     ("What is the wildcard exemption?","$600 plus up to $5,000 of unused homestead exemption. Can be applied to any property.")],
    """<div class="hero"><div class="container">
<h1>Georgia Bankruptcy Exemptions for Macon Filers</h1>
<p class="subtitle">Exemptions determine what property you keep when filing bankruptcy. Georgia does not allow federal exemptions -- Macon filers must use state exemptions.</p>
</div></div>

<section><div class="container">
<h2>Georgia Exemptions at a Glance</h2>
<div class="card">
<table>
<tr><th>Property</th><th>Exemption</th><th>Statute</th></tr>
<tr><td>Homestead (primary residence)</td><td>$21,500 ($43,000 married)</td><td>O.C.G.A. 44-13-100(a)(1)</td></tr>
<tr><td>Motor vehicle</td><td>$5,000</td><td>O.C.G.A. 44-13-100(a)(3)</td></tr>
<tr><td>Household goods</td><td>$600/item, $5,000 total</td><td>O.C.G.A. 44-13-100(a)(4)</td></tr>
<tr><td>Jewelry</td><td>$500</td><td>O.C.G.A. 44-13-100(a)(5)</td></tr>
<tr><td>Tools of the trade</td><td>$1,500</td><td>O.C.G.A. 44-13-100(a)(7)</td></tr>
<tr><td>Wildcard</td><td>$600 + up to $5,000 of unused homestead</td><td>O.C.G.A. 44-13-100(a)(6)</td></tr>
<tr><td>Health aids</td><td>Unlimited</td><td>O.C.G.A. 44-13-100(a)(9)</td></tr>
<tr><td>Retirement accounts</td><td>Fully exempt</td><td>O.C.G.A. 44-13-100(a)(2.1)</td></tr>
<tr><td>Social Security</td><td>Fully exempt</td><td>42 U.S.C. 407</td></tr>
<tr><td>Workers' compensation</td><td>Fully exempt</td><td>O.C.G.A. 34-9-84</td></tr>
<tr><td>Unemployment benefits</td><td>Fully exempt</td><td>O.C.G.A. 34-8-253</td></tr>
<tr><td>Alimony/child support</td><td>As needed for support</td><td>O.C.G.A. 44-13-100(a)(2)(D)</td></tr>
</table>
</div>
</div></section>

<section><div class="container">
<h2>Understanding the Wildcard Exemption</h2>
<div class="card">
<p>Georgia's wildcard is $600 plus up to $5,000 of unused homestead exemption:</p>
<ul>
<li><strong>Non-homeowner:</strong> $600 + $5,000 = $5,600 wildcard for any property</li>
<li><strong>Homeowner using full $21,500 homestead:</strong> $600 wildcard only</li>
<li><strong>Homeowner with less equity:</strong> $600 + (unused homestead, up to $5,000)</li>
</ul>
<p>Apply the wildcard to cash, bank accounts, tax refunds, vehicle equity, or anything else.</p>
</div>
</div></section>

<section><div class="container">
<h2>No Federal Exemptions in Georgia</h2>
<div class="card">
<p>Georgia <strong>opts out</strong> of the federal bankruptcy exemption system. You must use Georgia state exemptions -- you cannot choose federal exemptions.</p>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>What are Georgia's exemptions?</summary><div class="answer"><p>$21,500 homestead, $5,000 vehicle, $600/item personal property ($5,000 total), $600+$5,000 wildcard, fully exempt retirement and Social Security.</p></div></details>
<details class="faq-item"><summary>Can I use federal exemptions?</summary><div class="answer"><p>No. Georgia does not allow federal exemptions.</p></div></details>
<details class="faq-item"><summary>What is the wildcard?</summary><div class="answer"><p>$600 + up to $5,000 of unused homestead. Apply to any property. Non-homeowners get the full $5,600.</p></div></details>
</div></section>"""
)
if write_if_missing("macon/exemptions.html", html): created += 1

# macon/faq
html = page(
    "Macon Bankruptcy FAQ -- Common Questions Answered | Georgia Bankruptcy",
    "Answers to common bankruptcy questions for Macon, Georgia residents. Chapter 7, Chapter 13, exemptions, costs, timeline, and the M.D. Ga. courthouse.",
    "https://georgiabankruptcy.org/macon/faq.html",
    MAC_NAV,
    [("Georgia","https://georgiabankruptcy.org"),("Macon","https://georgiabankruptcy.org/macon/"),("FAQ","https://georgiabankruptcy.org/macon/faq.html")],
    [("How much does bankruptcy cost in Macon?","Chapter 7 filing fees are $338 and Chapter 13 fees are $313. Attorney fees in Macon typically range from $1,000-$1,800 for Chapter 7 and $2,500-$4,000 for Chapter 13."),
     ("Will I lose my house?","Georgia's homestead exemption protects up to $21,500 of equity. Chapter 13 can stop foreclosure and let you catch up."),
     ("How long does bankruptcy take?","Chapter 7: 3-4 months. Chapter 13: 3-5 years."),
     ("Will bankruptcy stop garnishment?","Yes. The automatic stay stops wage garnishment immediately upon filing."),
     ("Can I file without an attorney?","Yes (pro se), but it is not recommended due to complexity."),
     ("How often can I file?","Ch. 7 to Ch. 7: 8 years. Ch. 13 to Ch. 13: 2 years. Ch. 7 to Ch. 13: 4 years. Ch. 13 to Ch. 7: 6 years."),
     ("Where is the Macon courthouse?","U.S. Bankruptcy Court, 475 Mulberry St, Macon, GA 31201. Phone: (478) 752-3506."),
     ("Can I keep my car?","Georgia's $5,000 vehicle exemption protects your equity. The wildcard can cover additional equity.")],
    """<div class="hero"><div class="container">
<h1>Macon Bankruptcy FAQ</h1>
<p class="subtitle">Answers to the most common questions about filing bankruptcy in Macon and the Middle District of Georgia.</p>
</div></div>

<section><div class="container">
<h2>Frequently Asked Questions</h2>

<details class="faq-item"><summary>How much does bankruptcy cost in Macon?</summary><div class="answer"><p>Chapter 7 filing fees are $338 and Chapter 13 fees are $313. Attorney fees in the Macon area range from $1,000-$1,800 for Chapter 7 and $2,500-$4,000 for Chapter 13. Two credit counseling courses cost $25-50 total. Fee waivers available for Chapter 7 filers below 150% of poverty. <a href="https://howmuchdoesbankruptcycost.com" target="_blank" rel="noopener">National cost guide</a>.</p></div></details>

<details class="faq-item"><summary>Will I lose my house?</summary><div class="answer"><p>Georgia's homestead exemption protects up to $21,500 of equity ($43,000 for joint filers). Chapter 13 can stop foreclosure and let you catch up on missed payments. <a href="/macon/exemptions.html">Full exemptions guide</a>.</p></div></details>

<details class="faq-item"><summary>How long does bankruptcy take?</summary><div class="answer"><p>Chapter 7: 3-4 months from filing to discharge. Chapter 13: 3-5 year repayment plan. The <a href="https://341meeting.org" target="_blank" rel="noopener">341 meeting</a> is about 30 days after filing.</p></div></details>

<details class="faq-item"><summary>Will bankruptcy stop wage garnishment?</summary><div class="answer"><p>Yes. The <a href="https://automaticstay.org" target="_blank" rel="noopener">automatic stay</a> halts garnishment the moment your case is filed.</p></div></details>

<details class="faq-item"><summary>Can I file without an attorney?</summary><div class="answer"><p>Yes (pro se), but bankruptcy is complex. Mistakes can result in loss of property or dismissal. Most people benefit from professional help.</p></div></details>

<details class="faq-item"><summary>How often can I file?</summary><div class="answer"><p>Ch. 7 to Ch. 7: 8 years. Ch. 13 to Ch. 13: 2 years. Ch. 7 to Ch. 13: 4 years. Ch. 13 to Ch. 7: 6 years. <a href="https://1328f.com" target="_blank" rel="noopener">Check eligibility</a>.</p></div></details>

<details class="faq-item"><summary>Where is the Macon courthouse?</summary><div class="answer"><p>U.S. Bankruptcy Court, 475 Mulberry St, Macon, GA 31201. Phone: (478) 752-3506. Website: <a href="https://www.gamb.uscourts.gov" target="_blank" rel="noopener">gamb.uscourts.gov</a>.</p></div></details>

<details class="faq-item"><summary>Can I keep my car?</summary><div class="answer"><p>Georgia's $5,000 vehicle exemption protects your equity. If you owe more than the car is worth, there is no equity to protect. The wildcard ($600 + up to $5,000) can cover additional equity. <a href="https://keepmycarinbankruptcy.com" target="_blank" rel="noopener">Full car guide</a>.</p></div></details>

<details class="faq-item"><summary>What happens to my credit?</summary><div class="answer"><p>Bankruptcy stays on your report for 7 years (Ch. 13) or 10 years (Ch. 7). Most filers see improvement within 1-2 years. <a href="https://rebuildcreditafterbankruptcy.com" target="_blank" rel="noopener">Credit rebuilding guide</a>.</p></div></details>

<details class="faq-item"><summary>Can I discharge student loans?</summary><div class="answer"><p>Generally no, unless you prove undue hardship. This requires a separate adversary proceeding. Consult an attorney.</p></div></details>
</div></section>"""
)
if write_if_missing("macon/faq.html", html): created += 1

print(f"\n{'='*50}")
print(f"TOTAL CREATED: {created} pages")
print(f"{'='*50}")
