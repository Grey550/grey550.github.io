'use strict';

// Wrap the entire script in an IIFE for encapsulation
(function () {
  /**
   * Navbar toggle
   */

  const overlay = document.querySelector("[data-overlay]");
  const navOpenBtn = document.querySelector("[data-nav-open-btn]");
  const navbar = document.querySelector("[data-navbar]");
  const navCloseBtn = document.querySelector("[data-nav-close-btn]");
  const navLinks = document.querySelectorAll("[data-nav-link]");

  const navElemArr = [navOpenBtn, navCloseBtn, overlay];

  const toggleNav = function () {
    navbar.classList.toggle("active");
    overlay.classList.toggle("active");
  };

  const navToggleEvent = function (elem) {
    elem.forEach(function (element) {
      element.addEventListener("click", toggleNav);
    });
  };

  navToggleEvent(navElemArr);
  navToggleEvent(navLinks);

  /**
   * Header sticky & go to top
   */

  const header = document.querySelector("[data-header]");
  const goTopBtn = document.querySelector("[data-go-top]");

  const handleScroll = function () {
    if (window.scrollY >= 200) {
      header.classList.add("active");
      goTopBtn.classList.add("active");
    } else {
      header.classList.remove("active");
      goTopBtn.classList.remove("active");
    }
  };

  window.addEventListener("scroll", handleScroll);

  const updateLocationText = function () {
    const checkedLocations = {};
    const locationsCheckboxes = document.querySelectorAll(
      ".locations > .popover > li > input[type='checkbox']"
    );

    locationsCheckboxes.forEach(function (checkbox) {
      if (checkbox.checked) {
        checkedLocations[checkbox.getAttribute("data-id")] =
          checkbox.getAttribute("data-name");
      }
    });

    const locationText = Object.values(checkedLocations).join(", ") || "&nbsp;";
    document.querySelector("div.locations > h4").innerHTML = locationText;
  };

  const handleCheckboxChange = function (event) {
    if (event.target.matches(".locations > .popover > li > input[type='checkbox']")) {
      updateLocationText();
    }
  };

  document.addEventListener("change", handleCheckboxChange);

  // API Status Check
  $.get('http://your-api-url.com/api/v1/status/', function (data, textStatus) {
    if (textStatus === 'success') {
      if (data.status === 'OK') {
        $('#api_status').addClass('available');
      } else {
        $('#api_status').removeClass('available');
      }
    }
  }).fail(function () {
    // Handle AJAX failure here
    console.error("API status check failed");
  });

  // Function to append place articles
  const appendPlaceArticles = function (data) {
    const placesContainer = $('.places');

    data.forEach(function (place) {
      const article = `
        <article>
          <h2>${place.name}</h2>
          <div class="price_by_night"><p>$${place.price_by_night}</p></div>
          <div class="information">
            <div class="max_guest"><div class="guest_image"></div><p>${place.max_guest}</p></div>
            <div class="number_rooms"><div class="bed_image"></div><p>${place.number_rooms}</p></div>
            <div class="number_bathrooms"><div class="bath_image"></div><p>${place.number_bathrooms}</p></div>
          </div>
          <div class="description"><p>${place.description}</p></div>
        </article>
      `;
      placesContainer.append(article);
    });
  };

  // Initial places load
  $.ajax({
    type: 'POST',
    url: 'http://your-api-url.com/api/v1/places_search',
    data: '{}',
    dataType: 'json',
    contentType: 'application/json',
    success: appendPlaceArticles,
  }).fail(function () {
    // Handle AJAX failure here
    console.error("Initial places load failed");
  });

  // Filters button click event
  $('.filters > button').click(function () {
    $('.places > article').remove();
    const requestData = {
      activities: Object.keys(checkedActivities),
      states: Object.keys(checkedStates),
      cities: Object.keys(checkedCities),
    };

    $.ajax({
      type: 'POST',
      url: 'http://your-api-url.com/api/v1/places_search',
      data: JSON.stringify(requestData),
      dataType: 'json',
      contentType: 'application/json',
      success: appendPlaceArticles,
    }).fail(function () {
      // Handle AJAX failure here
      console.error("Filter places failed");
    });
  });
})();
