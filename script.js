
fetch('data/entries.json')
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById('entries-container');
    data.forEach(entry => {
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
            <img src="assets/images/${entry.image}" alt="PS5 Pro #${entry.number}">
            <h2>#${entry.number}</h2>
            <p><strong>${entry.name || 'Anonymous'}</strong></p>
            <p>${entry.notes || ''}</p>
            <div class="socials">
                ${entry.socials?.discord ? 'Discord: ' + entry.socials.discord + '<br>' : ''}
                ${entry.socials?.psn ? 'PSN: ' + entry.socials.psn + '<br>' : ''}
                ${entry.socials?.twitter ? 'Twitter: ' + entry.socials.twitter : ''}
            </div>
        `;
        container.appendChild(card);
    });
});
