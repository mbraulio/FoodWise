const express = require('express');
const app = express();
const PORT = 3000;

const alimentos = [
    "Manzana",
    "Banana",
    "Zanahoria",
    // ... añade más alimentos aquí
];

app.use(express.static('public'));
app.use(express.json());

app.get('/buscar', (req, res) => {
    let query = req.query.q.toLowerCase();
    let coincidencias = alimentos.filter(a => a.toLowerCase().includes(query));
    res.json(coincidencias);
});

app.listen(PORT, () => {
    console.log(`Servidor iniciado en http://localhost:${PORT}`);
});