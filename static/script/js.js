const box = document.getElementById('first');

box.addEventListener('mouseover',function(){
    box.style.backgroundColor = 'white';
    box.style.transform = 'scale(1.08)';
    box.style.color = 'black';

    const children = box.querySelectorAll('*');  // Select all children
    children.forEach(child => {
        child.style.color = 'black';  // Set text color to black for all child elements
    });
});

box.addEventListener('mouseout', function() {
    box.style.backgroundColor = ''; 
    box.style.transform = 'scale(1)';  // Reset the background color
    box.style.color = 'white';  
    
    const children = box.querySelectorAll('*');  // Select all children
    children.forEach(child => {
        child.style.color = '';  // Set text color to black for all child elements
    });// Reset the text color
});

const box2 = document.getElementById('second');

box2.addEventListener('mouseover',function(){
    box2.style.backgroundColor = 'white';
    box2.style.transform = 'scale(1.08)';
    box2.style.color = 'white';

    const children = box2.querySelectorAll('*');  // Select all children
    children.forEach(child => {
        child.style.color = 'black';  // Set text color to black for all child elements
    });
});

box2.addEventListener('mouseout', function() {
    box2.style.backgroundColor = '';
    box2.style.transform = 'scale(1)'; // Reset the background color
    box2.style.color = '';  // Reset the text color

    const children = box2.querySelectorAll('*');  // Select all children
    children.forEach(child => {
        child.style.color = '';  // Set text color to black for all child elements
    });// Reset the text color
});

const box3 = document.getElementById('third');

box3.addEventListener('mouseover',function(){
    box3.style.backgroundColor = 'white';
    box3.style.transform = 'scale(1.08)';
    box3.style.color = 'white';

    const children = box3.querySelectorAll('*');  // Select all children
    children.forEach(child => {
        child.style.color = 'black';  // Set text color to black for all child elements
    });
});

box3.addEventListener('mouseout', function() {
    box3.style.backgroundColor = '';
    box3.style.transform = 'scale(1)'; // Reset the background color
    box3.style.color = 'white';  // Reset the text color

    const children = box3.querySelectorAll('*');  // Select all children
    children.forEach(child => {
        child.style.color = '';  // Set text color to black for all child elements
    });// Reset the text color
});

const box4 = document.getElementById('fourth');

box4.addEventListener('mouseover',function(){
    box4.style.backgroundColor = 'white';
    box4.style.transform = 'scale(1.08)';
    box4.style.color = 'black';

    const children = box4.querySelectorAll('*');  // Select all children
    children.forEach(child => {
        child.style.color = 'black';  // Set text color to black for all child elements
    });
});

box4.addEventListener('mouseout', function() {
    box4.style.backgroundColor = '';
    box4.style.transform = 'scale(1)'; // Reset the background color
    box4.style.color = 'white';  // Reset the text color

    const children = box4.querySelectorAll('*');  // Select all children
    children.forEach(child => {
        child.style.color = '';  // Set text color to black for all child elements
    });// Reset the text color
});

