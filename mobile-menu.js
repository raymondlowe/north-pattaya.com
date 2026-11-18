/*
 * Mobile Menu JavaScript for Corralejo Fuerteventura
 * Implements sliding menu functionality similar to recoleta-ba.com
 */

$(document).ready(function() {
  // Mobile menu toggle functionality
  const $mobileToggle = $('.mobile-menu-toggle');
  const $mobileOverlay = $('.mobile-menu-overlay');
  const $mobileBackdrop = $('.mobile-menu-backdrop');
  const $mobileClose = $('.mobile-menu-close');
  
  // Open mobile menu
  $mobileToggle.on('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    openMobileMenu();
  });
  
  // Close mobile menu
  $mobileClose.on('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    closeMobileMenu();
  });
  
  // Close menu when clicking backdrop
  $mobileBackdrop.on('click', function(e) {
    e.preventDefault();
    closeMobileMenu();
  });
  
  // Close menu when clicking outside
  $(document).on('click', function(e) {
    if (!$(e.target).closest('.mobile-menu-overlay, .mobile-menu-toggle').length) {
      closeMobileMenu();
    }
  });
  
  // Close menu when pressing Escape key
  $(document).on('keydown', function(e) {
    if (e.keyCode === 27) { // Escape key
      closeMobileMenu();
    }
  });
  
  // Close menu when clicking a menu link (for single page navigation)
  $('.mobile-nav-menu a').on('click', function() {
    closeMobileMenu();
  });
  
  function openMobileMenu() {
    $mobileOverlay.addClass('active');
    $mobileBackdrop.addClass('active');
    $('body').addClass('menu-open').css('overflow', 'hidden');
  }
  
  function closeMobileMenu() {
    $mobileOverlay.removeClass('active');
    $mobileBackdrop.removeClass('active');
    $('body').removeClass('menu-open').css('overflow', '');
  }
  
  // Handle window resize
  $(window).on('resize', function() {
    if ($(window).width() >= 768) {
      closeMobileMenu();
    }
  });
  
  // Prevent menu from opening on desktop
  if ($(window).width() >= 768) {
    closeMobileMenu();
  }
});

// Prevent body scroll when menu is open
$('body').on('touchmove', function(e) {
  if ($('body').hasClass('menu-open')) {
    e.preventDefault();
  }
});