const http = require('http')


const server = http.createServer((req, res) => {
    res.setHeader('Content-Type', 'text/html')
    res.write('<html>')
    res.write('<body>Hello')
    res.write('</body>')
    res.write('</html>')
    res.end()
})

server.listen(8000)
