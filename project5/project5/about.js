// // ფეიდ ინი ტექსტების სქროლის დროს
// function fadeInOnScroll() {
//   const fadeElements = document.querySelectorAll('.text-section h2, .text-section p');

//   fadeElements.forEach(el => {
//     const rect = el.getBoundingClientRect();
//     if (rect.top < window.innerHeight - 100) {
//       el.style.opacity = '1';
//       el.style.transform = 'translateY(0)';
//       el.style.transition = 'opacity 0.8s ease-out, transform 0.8s ease-out';
//     }
//   });
// }

// value-card-ების JS hover ეფექტი (მინიმალური, ფერების კონტროლი)
// function setupValueCards() {
//   const cards = document.querySelectorAll('.value-card');

//   cards.forEach(card => {
//     card.addEventListener('mouseenter', () => {
//       card.style.backgroundColor = '#00bcd4';
//       card.style.color = '#121212';
//       card.querySelector('.value-icon').style.color = '#121212';
//       card.style.boxShadow = '0 15px 40px rgba(0,188,212,0.8)';
//       card.style.cursor = 'default';
//     });

//     card.addEventListener('mouseleave', () => {
//       card.style.backgroundColor = '#1f1f1f';
//       card.style.color = '#eee';
//       card.querySelector('.value-icon').style.color = '#00bcd4';
//       card.style.boxShadow = '0 8px 20px rgba(0,188,212,0.4)';
//     });
//   });
// }

// // Scroll to top ღილაკი
// function createScrollTopButton() {
//   const btn = document.createElement('button');
//   btn.textContent = '↑ ზემოთ';
//   btn.id = 'scrollTopBtn';
//   btn.style.position = 'fixed';
//   btn.style.bottom = '30px';
//   btn.style.right = '30px';
//   btn.style.padding = '10px 15px';
//   btn.style.fontSize = '18px';
//   btn.style.backgroundColor = '#00bcd4';
//   btn.style.color = '#121212';
//   btn.style.border = 'none';
//   btn.style.borderRadius = '8px';
//   btn.style.cursor = 'pointer';
//   btn.style.boxShadow = '0 4px 10px rgba(0,188,212,0.7)';
//   btn.style.display = 'none';
//   btn.style.zIndex = '9999';
//   btn.style.transition = 'opacity 0.3s ease';

//   document.body.appendChild(btn);

//   btn.addEventListener('click', () => {
//     window.scrollTo({ top: 0, behavior: 'smooth' });
//   });

//   window.addEventListener('scroll', () => {
//     if (window.scrollY > 300) {
//       btn.style.display = 'block';
//       btn.style.opacity = '1';
//     } else {
//       btn.style.opacity = '0';
//       setTimeout(() => { btn.style.display = 'none'; }, 300);
//     }
//   });
// }

// document.addEventListener('DOMContentLoaded', () => {
//   setupValueCards();
//   createScrollTopButton();

//   // დაწყნარებული opacity და ტრანსფორმები პირველად
//   const fadeElements = document.querySelectorAll('.text-section h2, .text-section p');
//   fadeElements.forEach(el => {
//     el.style.opacity = '0';
//     el.style.transform = 'translateY(30px)';
//   });

//   // სკროლის დროს ფეიდ ინი
//   window.addEventListener('scroll', fadeInOnScroll);
//   fadeInOnScroll(); // თუ თავიდან ჩანს გვერდი, მაშინაც შეამოწმოს
// });
