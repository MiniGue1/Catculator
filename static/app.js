(function(){
  const display = document.getElementById('display')
  const buttons = document.querySelectorAll('.buttons button')
  const equals = document.getElementById('equals')
  const clear = document.getElementById('clear')
  const modal = document.getElementById('catModal')
  const closeCat = document.getElementById('closeCat')

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      const val = btn.dataset.value
      if (val !== undefined) {
        display.value = display.value + val
      }
    })
  })

  clear.addEventListener('click', () => display.value = '')

  equals.addEventListener('click', showCat)

  // Enter and = keys trigger the cat
  window.addEventListener('keydown', (e) => {
    if (e.key === '=' || e.key === 'Enter') {
      e.preventDefault();
      showCat()
    }
    // allow typing numbers and operators
    const allowed = '0123456789.+-*/()%'
    if (allowed.indexOf(e.key) !== -1) {
      display.value = display.value + e.key
      e.preventDefault()
    }
    if (e.key === 'Backspace') {
      display.value = display.value.slice(0, -1)
    }
    if (e.key.toLowerCase() === 'c') {
      display.value = ''
    }
  })

  function showCat(){
    modal.setAttribute('aria-hidden', 'false')
  }

  closeCat.addEventListener('click', () => modal.setAttribute('aria-hidden', 'true'))

  // Close on outside click
  modal.addEventListener('click', (e) => { if (e.target === modal) modal.setAttribute('aria-hidden', 'true') })

})()
