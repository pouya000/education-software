// ----------------------------- puya start -----------------------
// let date = document.querySelector('.date1');
// console.log(date);
const imageProfile = document.querySelector('.image-profile img');
console.log('imageProfile: ', imageProfile)
const profile = document.querySelector('.profile');
const liInProfile = document.querySelectorAll('.profile ul');
const cartitemcontent = document.querySelectorAll('.item-score');
const closePopupTest = document.querySelector('.popup-test-container .popup-test .fa-times');
// const goToTop = document.querySelector('.go-to-top');
const popupTest = document.querySelector('.popup-test');
const popupTestContainer = document.querySelector('.popup-test-container');
const overlay = document.querySelector('.overlay');
const lessonScore = document.querySelector('.lesson-score');
const signupButton = document.querySelector('.header-signup-button');
const popup = document.querySelector('.popup');
const shoppingCartBox = document.querySelector('.shopping-cart-box');
const closePopup = document.querySelector('.header-signup i');
const shoppingIcon = document.querySelector('.fa-user-lock');
const hamMenue = document.getElementById('ham-menue');
const openHamberger = document.getElementById('navForHamberger');
const closeHamberger = document.querySelector('.navForHamberger i');
const mainNav = document.querySelector('.main-nav');

// -------------- slider ------------------
// const sliderr = document.querySelector('.sugestion-exam-container .exam-item');
// const sliderr2 = document.querySelectorAll('.sugestion-exam-container .exam-item');
const carousel = document.querySelector('.sugestion-exam-container');
const next = document.querySelector('.sugestion-exams .fa-angle-right');
const prev = document.querySelector('.sugestion-exams .fa-angle-left');
let summ = 0;

hamMenue.addEventListener('click', openHambergerMenue)
// closeHamberger.addEventListener('click', closeHambergerMenue)
// closePopupTest.addEventListener('click', closePopupTestIcon);
imageProfile.addEventListener('click', show_close);
console.log('is clicked out ..');
function show_close() {
    console.log('is clicked..');
    profile.classList.toggle('active');
}

// signupButton.addEventListener('click', showModal);
// closePopup.addEventListener('click', closeModal);
// shoppingIcon.addEventListener('click', showShoppingBox);
// next.addEventListener('click', slider);
// prev.addEventListener('click', slider2);
// sliderr.addEventListener('transitionend', slider3);



function showPopupTest() {
    // console.log(e.target)
    // e.preventDefault();
    popupTestContainer.classList.add('active');
    document.body.style.overflow = 'hidden';
}

let direct;

cartitemcontent.forEach((score) => {
    let tprice = (score.innerHTML.match(/\d+/)[0]);
    summ += Number(tprice);
    totalPrice.innerText = `${summ} امتیاز`;
})

liInProfile.forEach(item=>{
    item.addEventListener('click',closeProfile)
})

// const courseItem = document.querySelectorAll('.exam-item .item');
// console.log('courseItem ', courseItem[0]);
// const width = window.getComputedStyle(courseItem[0]).getPropertyValue('width');
// console.log('width ',width);
// --------------------------------
// console.log(examcontainer)


function closeProfile(){
    profile.classList.remove('active');
}

function closePopupTestIcon() {
    popupTestContainer.classList.remove('active')
    document.body.style.overflow = 'visible';
}

function slider() {
    direct = -1;
    // carousel.style.justifyContent = 'flex-start';
    sliderr.style.transform = `translate(${width})`;
    // console.log(sliderr.firstElementChild);
}

function slider2() {
    if (direct === -1) {
        direct = 1;
        sliderr.append(sliderr.firstElementChild);
    }
    // carousel.style.justifyContent = 'flex-end';
    sliderr.style.transform = `translate(-${width})`;
}

function slider3() {
    if (direct === 1) {
        console.log(sliderr.firstElementChild);
        sliderr.prepend(sliderr.lastElementChild);
    } else {
        console.log(sliderr.firstElementChild);
        sliderr.append(sliderr.firstElementChild);
    }
    sliderr.style.transition = 'none';
    sliderr.style.transform = 'translate(0)';
    setTimeout(() => {
        sliderr.style.transition = 'all 900ms';
    }, false)
}

function showShoppingBox() {
    shoppingCartBox.classList.toggle('active');
    shoppingCartBox.style.opacity = 1;
    // document.body.style.overflow = 'hidden';
}

function openHambergerMenue() {
    // console.log(openHamberger);
    openHamberger.classList.add('active');
    mainNav.style.transform = 'translateX(-250px)';
    document.body.style.overflow = 'hidden';

}

function closeHambergerMenue() {
    openHamberger.classList.remove('active');
    mainNav.style.transform = 'translateX(10px)';
    document.body.style.overflow = 'visible';
}

function closeModal() {
    popup.classList.remove('active');
    document.body.style.overflow = 'visible';

}

// function showModal(e) {
// 	e.preventDefault();
// 	popup.classList.add('active');
// 	document.body.style.overflow = 'hidden';
//
// }

counterDouwn();

setInterval(counterDouwn, 1000);


// window.addEventListener('scroll', () => {
//     if (window.scrollY > 700) {
//         goToTop.style.display = 'block';
//     } else if (window.scrollY < 700) {
//         goToTop.style.display = 'none';
//     }
// })

// goToTop.addEventListener('click', () => {
//     window.scrollTo({top: 0, behavior: `smooth`});
// })

const datePublish = 'Feb 17 2025 '
const counterDouwn = () => {
    const dayDiv = document.querySelector('.day')
    const hourDiv = document.querySelector('.hour')
    const minuteDiv = document.querySelector('.minute')
    const secondDiv = document.querySelector('.second')
    const curentDate = new Date();
    const pDate = new Date(datePublish);
    let totalSeconds = (pDate - curentDate) / 1000;
    let days = (totalSeconds) / 86400;
    let temp1 = (totalSeconds) % 86400;

    let hours = (temp1) / 3600;
    let temp2 = (temp1) % 3600;

    let minutes = temp2 / 60;
    let temp3 = (temp2) % 60;

    let seconds = (temp3) % 60;
    dayDiv.innerText = `: ${Math.floor(days)} `;
    hourDiv.innerText = `: ${Math.floor(hours)} `;
    minuteDiv.innerText = `: ${Math.floor(minutes)} `;
    secondDiv.innerText = Math.floor(seconds);

    console.log('days,hours,minutes,totalSeconds', days, hours, minutes, totalSeconds);
}
// ------------------------------ account ( register & login)-----------------------------------








