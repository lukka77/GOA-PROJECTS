// 3. Hero Section Typing Text Effect
  const heroHeading = document.querySelector('.hero-content h1');
  const text = heroHeading.innerText;
  heroHeading.innerText = '';
  let index = 0;

  function typeWriter() {
    if (index < text.length) {
      heroHeading.innerHTML += text.charAt(index);
      index++;
      setTimeout(typeWriter, 40);
    }
  }

  setTimeout(typeWriter, 500);

// 4. Button Hover Animation Effect
  const buttons = document.querySelectorAll('.btn, .btn-small');

  buttons.forEach(btn => {
    btn.addEventListener('mouseover', () => {
      btn.style.transform = 'scale(1.05)';
    });
    btn.addEventListener('mouseout', () => {
      btn.style.transform = 'scale(1)';
    });
  });
// });
