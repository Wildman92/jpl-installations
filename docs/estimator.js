(function () {
  const bid = document.getElementById("bid");
  if (!bid) return;

  const box = document.createElement("section");
  box.id = "estimator";
  box.innerHTML = `
    <div class="wrap">
      <div class="qbox" style="margin-bottom:10px;border-color:#262c36;">
        <span class="stag">Interactive Project Calculator</span>
        <h2>Instant Flooring &amp; Fencing Ballpark Estimator</h2>
        <p style="color:var(--mut);margin-bottom:20px;">Select your scope and approximate footage for a rough Mid-Willamette Valley installed range prior to Jorey's free on-site measurement.</p>
        <div class="fg">
          <label>Material / Service Spec
            <select id="est-spec">
              <option value="6.5,9.5,sq ft,Click-Lock Waterproof LVP">Flooring — Click-Lock Waterproof LVP ($6.50–$9.50/sq ft)</option>
              <option value="5.5,8.5,sq ft,Commercial Glue-Down LVP / Carpet Tile">Flooring — Commercial Glue-Down LVP / Carpet Tile ($5.50–$8.50/sq ft)</option>
              <option value="42,58,linear ft,6ft Cap & Trim Cedar Fence">Fencing — 6ft Cap &amp; Trim Cedar Fence ($42–$58/lin ft)</option>
              <option value="48,65,linear ft,Vinyl Privacy Fence">Fencing — Vinyl Privacy Fence ($48–$65/lin ft)</option>
              <option value="26,38,linear ft,Galvanized / Black Chain Link">Fencing — Galvanized / Black Chain Link ($26–$38/lin ft)</option>
            </select>
          </label>
          <label>Approximate Footage (<span id="est-unit">sq ft</span>)
            <input type="number" id="est-qty" value="650" min="10" max="25000">
          </label>
        </div>
        <div style="background:var(--bg);border:1px solid rgba(234,179,8,.45);border-radius:10px;padding:18px;margin-top:6px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;">
          <div>
            <div style="font-size:.8rem;color:var(--mut);text-transform:uppercase;letter-spacing:.06em;">Estimated Installed Range (Materials + Labor)</div>
            <div id="est-out" style="font-size:1.55rem;font-weight:800;color:#facc15;">$4,225 – $6,175</div>
          </div>
          <button type="button" id="est-apply" class="btn btn-s" style="border:none;cursor:pointer;">Load Into Quote Form ↓</button>
        </div>
      </div>
    </div>`;

  bid.parentNode.insertBefore(box, bid);

  const specEl = document.getElementById("est-spec");
  const qtyEl = document.getElementById("est-qty");
  const unitEl = document.getElementById("est-unit");
  const outEl = document.getElementById("est-out");

  function calc() {
    const [low, high, unit] = specEl.value.split(",");
    const qty = Math.max(1, Number(qtyEl.value) || 0);
    unitEl.textContent = unit;
    const min = Math.round(qty * Number(low)).toLocaleString();
    const max = Math.round(qty * Number(high)).toLocaleString();
    outEl.textContent = `$${min} – $${max}`;
  }

  specEl.addEventListener("change", () => {
    const unit = specEl.value.split(",")[2];
    qtyEl.value = unit === "linear ft" ? 110 : 650;
    calc();
  });
  qtyEl.addEventListener("input", calc);

  document.getElementById("est-apply").addEventListener("click", () => {
    const [, , unit, label] = specEl.value.split(",");
    const notes = bid.querySelector("textarea");
    if (notes) {
      notes.value = `Ballpark Estimate: ~${qtyEl.value} ${unit} of ${label} (${outEl.textContent}). Requesting free on-site measurement.`;
    }
    bid.scrollIntoView({ behavior: "smooth" });
  });
})();
