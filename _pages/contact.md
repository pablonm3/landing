---
layout: default
permalink: /contact/
title: Contact
nav: true
nav_order: 4
---

<div class="post">
  <div class="header-bar">
    <h1>Contact</h1>
    <h3>Get in touch about your NLP problem and I'll send you an NLP strategy for FREE. No strings attached.</h3>
  </div>

  <div class="contact-form">
    <form id="contactForm" onsubmit="handleSubmit(event)">
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" class="form-control" id="name" name="name" required>
      </div>
      
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" class="form-control" id="email" name="email" required>
      </div>
      
      <div class="form-group">
        <label for="message">Tell me more about your usecase:</label>
        <textarea class="form-control" id="message" name="message" rows="5" required></textarea>
      </div>
      
      <button type="submit" class="btn btn-primary">Send Message</button>
    </form>
  </div>
</div>

<style>
.contact-form {
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-control {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.btn-primary {
  background-color: var(--global-theme-color);
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-primary:hover {
  opacity: 0.8;
}

.header-bar {
  padding: 10px 0;
}
</style>

<script>
async function handleSubmit(event) {
    event.preventDefault();
    
    const formData = new FormData(event.target);
    try {
        const response = await fetch('https://pablomarino.com/api/submit', {
            method: 'POST',
            body: formData
        });
        
        alert('Thank you for your message! I will get back to you soon.');
    } catch (error) {
        alert('Something went wrong. Please email me at pablo@pablomarino.com');
        console.error('Error submitting form:', error);
    }
}
</script>
