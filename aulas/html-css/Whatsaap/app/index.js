const sidebarButtons = document.querySelectorAll('.side-button');


sidebarButtons.forEach((button) => {
  button.addEventListener('click', () => {
    sidebarButtons.forEach((item) => item.classList.remove('active'));
    button.classList.add('active');
  });
});


const chatItems = document.querySelectorAll('.chat');
const contactName = document.getElementById('contact-name');
const contactMembers = document.getElementById('contact-members');
let contactAvatar = document.querySelector('.contact .avatar');


chatItems.forEach((item) => {
  item.addEventListener('click', () => {
    chatItems.forEach((chat) => chat.classList.remove('active'));
    item.classList.add('active');


    contactName.textContent = item.dataset.contact;
    contactMembers.textContent = item.dataset.members;


    const avatar = item.querySelector('.avatar').cloneNode(true);
    avatar.classList.add('small');
    contactAvatar.replaceWith(avatar);
    contactAvatar = avatar;
  });
});











