const game = function () {
    const wrapper = document.querySelector('.game-wrapper');
    const row = 4;
    const col = 4;
    const symbols = "ABCDEFGHIJKLMNOPRSTUY123456789".split("")
    let cells = []
    let previousCellIndex = null;
    let canPlay = false;
    //create grid
    const grid = document.createElement('div')
    grid.classList.add('grid')
    wrapper.appendChild(grid)

    //create info panel
    const infoPanel = document.createElement('div')
    infoPanel.classList.add('info-panel')
    wrapper.appendChild(infoPanel)

    //create cells
    for (let i = 0; i < row * col; i += 2) {
        const symbol = randomSymbol()
        for (let j = 0; j < 2; j++) {
            const currentCellIndex = i + j;
            const cellElement = document.createElement('div')
            cellElement.classList.add('cell')
            cellElement.style.width = `${100 / col}%`
            cellElement.innerText = symbol;

            const cell = {
                symbol: symbol,
                element: cellElement,
                hasMatch: false
            }

            setTimeout(() => {
                cellElement.classList.add('hide')
            }, randomInt(2500, 3500))

            if (currentCellIndex > 2) {
                const previousRandomIndex = randomInt(0, i)
                cells[currentCellIndex] = cells[previousRandomIndex];
                cells[previousRandomIndex] = cell;

            } else {
                cells[currentCellIndex] = cell;
                console.log(cell)
            }
        }
    }

    //add all elements
    cells.forEach((item, index) => {
        item.element.addEventListener('click', () => cellClickHandler(index))
        grid.appendChild(item.element)
        canPlay = true
    })

    function randomSymbol() {
        const symbolIndex = randomInt(0, symbols.length - 1)
        const symbol = symbols[symbolIndex]
        //delete symbol from symbols
        symbols.splice(symbolIndex, 1)
        return symbol;
    }

    function randomInt(min, max) {
        return Math.round(Math.random() * (max - min)) + min
    }

    // function cellClickHandler(index) {
    //     const cellElement = cells[index].element
    //     if (canPlay && cellElement.classList.contains('hide')) {
    //         canPlay = false;
    //         cellElement.classList.remove('hide')
    //         if (previousCellIndex === null) {
    //             //first click
    //             previousCellIndex = index;
    //             canPlay = true
    //         } else {
    //             //console.log(cells[previousCellIndex].symbol,cells[index].symbol)
    //             if (cells[previousCellIndex].symbol === cells[index].symbol) {
    //                 cells[previousCellIndex].hasMatch = true;
    //                 cells[index].hasMatch = true
    //                 showInfo('MATCH', 'green')
    //                 setTimeout(() => {
    //                     previousCellIndex = null;
    //                     canPlay = true
    //                 }, 500)
    //             } else {
    //                 showInfo('NO MATCH', 'red')
    //                 cells[previousCellIndex].element.classList.add('hide')
    //                 cellElement.classList.add('hide')
    //                 previousCellIndex = null;
    //                 canPlay = true
    //             }
    //
    //         }
    //     }
    // }

    function showInfo(message, type) {
        infoPanel.innerHTML = `<span class='${type}'>${message}</span>`
    }

};

game();