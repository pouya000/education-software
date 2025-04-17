import grid from './grid.js'
grid.init()
const points = document.getElementById('points');
document.addEventListener('keyup',function(e){
    let direction = null;
    if(e.key==='ArrowUp'){
        direction = "UP"
    }
    else if(e.key==='ArrowRight'){
        direction='RIGHT'
    }
    else if(e.key==='ArrowLeft'){
        direction='LEFT'
    }
    else if(e.key==='ArrowDown'){
        direction='DOWN'
    }
    if(direction!==null){
        const numberElements = document.querySelectorAll('.number');
        let sum = 2;
        numberElements.forEach(numberElement=>sum +=Number(numberElement.innerText))
        points.innerHTML = `<button disabled> امتیاز : ${sum}</button>`
        grid.slide(direction)
    }
    return false;
})