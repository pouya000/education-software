import number from './number.js'
const infoelement = document.getElementById('info')
const grid={
    gridElement : document.getElementsByClassName('grid')[0],
    cells:[],
    playable:false,
    directionRoots:{
        'UP':[1,2,3,4],
        'RIGHT':[4,8,12,16],
        'DOWN':[13,14,15,16],
        'LEFT':[1,5,9,13]
    },
    init:function(){
        const cellElements = document.getElementsByClassName('cell');
        let cellIndex = 1;
        for(let cellElement of cellElements){
           // console.log(cellElement.offsetTop,cellElement.offsetLeft)
            grid.cells[cellIndex]={
                element:cellElement,
                top:cellElement.offsetTop,
                left:cellElement.offsetLeft,
                number:null
            }
            cellIndex++
        }
        //start game
        number.spawn();
        this.playable = true

    },
    emptyRandomCellIndex:function(){
        let emptyCells = [];
        for (let i=1 ; i< this.cells.length; i++) {
            if(this.cells[i].number===null){
                emptyCells.push(i)
            }
        }
        if(emptyCells.length===0){
            //no empty cell, game over
        }
        return emptyCells[Math.floor(Math.random()*emptyCells.length)]
    },
    slide:function(direction){
        if(!this.playable){
            return false
        }

        //set playable to false to prevent continues slides
        this.playable = false;

        //get directions grid root index
        const roots = this.directionRoots[direction]
        //indexs increment or decrement depend on direction
        let increment = (direction==='RIGHT' || direction==='DOWN')?-1 :1
        //indexes move by
        increment *=(direction==='UP' || direction==='DOWN')?4:1;

        for (let i = 0; i < roots.length; i++) {
            const root = roots[i]

            for (let j = 1; j < 4; j++){
                const cellIndex = root + (j*increment)
               //console.log(cellIndex)
               const cell = this.cells[cellIndex]

               if(cell.number!==null){
                   let moveToCell = null;
                   for(let k =j-1;k>0;k--){

                      const foreCellIndex = root +(k*increment)
                      const foreCell = this.cells[foreCellIndex];
                      if(foreCell.number===null){
                          //the cell is empty, move and check next cell
                          moveToCell = foreCell
                      }else if(cell.number.dataset.value===foreCell.number.dataset.value){
                          moveToCell = foreCell
                      }
                      else{
                          break;
                      }
                   }
                   if(moveToCell!==null){
                       number.moveTo(cell,moveToCell)
                   }
               }

            }

        }

        setTimeout(()=>{

            if(number.spawn()){
                grid.playable = true;
            }else{
              infoelement.innerHTML = `<button onClick="location.reload()">شروع مجدد</button>"`;
              const h1Element = document.createElement('h1');
              h1Element.style.color = 'red';
              h1Element.innerText = 'GameOver!!';
              infoelement.appendChild(h1Element)
            }
        },500)
    }
}
export default grid;