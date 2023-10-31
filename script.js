const input = document.querySelector('input');
const resultadosDiv = document.querySelector('.resultados');

input.addEventListener('input', async () => {
    let query = input.value;
    if(query) {
        let respuesta = await fetch(`/buscar?q=${query}`);
        let alimentos = await respuesta.json();
        mostrarResultados(alimentos);
    } else {
        resultadosDiv.innerHTML = '';
    }
});

function mostrarResultados(alimentos) {
    resultadosDiv.innerHTML = '';
    alimentos.forEach(a => {
        resultadosDiv.innerHTML += `<p>${a}</p>`;
    });
}