const https = require('https');

const ids = [
    "tt33244668", // Anaconda
    "tt33479805", // Killer Whale
    "tt32247012", // A Series of Unfortunate Dates
    "tt6946962",  // Wolfe
    "tt39742493", // Far End of the Sea
    "tt31691565"  // Good Cop / Bad Cop
];

function fetchPoster(id) {
    const options = {
        hostname: 'www.imdb.com',
        path: `/title/${id}/`,
        headers: {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }
    };

    https.get(options, (res) => {
        let data = '';
        res.on('data', chunk => data += chunk);
        res.on('end', () => {
            const match = data.match(/meta property="og:image" content="([^"]+)"/);
            if (match) {
                console.log(`${id}: ${match[1]}`);
            } else {
                console.log(`${id}: Not found`);
            }
        });
    }).on('error', (e) => {
        console.error(`${id}: Error - ${e.message}`);
    });
}

ids.forEach(fetchPoster);
