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



//   .chat-header .tools button { width: 25px; font-size: 15px; }
//   .bubble { max-width: 85%; padding: 8px 10px; font-size: 13px; }
//   .composer { gap: 4px; padding: 6px; }
//   .composer button { width: 27px; font-size: 16px; }
//   .composer .mic { flex-basis: 36px; width: 36px; height: 36px; }
// }








