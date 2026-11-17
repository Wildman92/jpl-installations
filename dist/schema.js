(function () {
  const data = {
    "@context": "https://schema.org",
    "@type": "HomeAndConstructionBusiness",
    "name": "JPL Installations Construction Company",
    "slogan": "Build • Install • Improve",
    "foundingDate": "2017",
    "telephone": "+1-971-382-2083",
    "address": {
      "@type": "PostalAddress",
      "postOfficeBoxNumber": "PO Box 20541",
      "addressLocality": "Keizer",
      "addressRegion": "OR",
      "postalCode": "97307",
      "addressCountry": "US"
    },
    "areaServed": ["Keizer, OR", "Salem, OR", "Albany, OR", "Lebanon, OR", "Scio, OR", "Jefferson, OR", "Aumsville, OR", "Sublimity, OR"],
    "knowsAbout": ["Luxury Vinyl Plank Installation", "Commercial Glue-Down Flooring", "Commercial Carpet Tile", "6ft Cedar Fencing", "Vinyl Fencing", "Chain Link Fencing"],
    "sameAs": ["https://facebook.com"]
  };
  const s = document.createElement("script");
  s.type = "application/ld+json";
  s.textContent = JSON.stringify(data);
  document.head.appendChild(s);

  const bar = document.createElement("div");
  bar.className = "mbar";
  bar.innerHTML = '<a href="tel:9713822083" class="mcall">📞 Call (971) 382-2083</a><a href="#bid" class="mbid">Get Free Bid →</a>';
  document.body.appendChild(bar);
})();
