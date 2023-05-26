'use strict';

const btn = document.querySelector('.btn-country');
const countriesContainer = document.querySelector('.countries');

///////////
const countriesAPI = 'https://restcountries.com/v2/';

const renderHTML = function (data, className) {
  const html = `
    <article class="country ${className}">
      <img class="country__img" src="${data.flag}" />
      <div class="country__data">
        <h3 class="country__name">${data.name}</h3>
        <h4 class="country__region">${data.region}</h4>
        <p class="country__row"><span>👫</span>${(
          +data.population / 1000000
        ).toFixed(1)}</p>
        <p class="country__row"><span>🗣️</span>${data.languages[0].name}</p>
        <p class="country__row"><span>💰</span>${data.currencies[0].name}</p>
      </div>
    </article>
  `;

  countriesContainer.insertAdjacentHTML('beforeend', html);
  countriesContainer.style.opacity = 1;
};

const getCountryData = function (country) {
  // old way of handling AJAX calls
  const request = new XMLHttpRequest();

  request.open('GET', countriesAPI + 'name/' + country);
  request.send();

  request.addEventListener('load', function () {
    console.log(this);
    const data = JSON.parse(this.responseText)[0];
    console.log(data);

    const html = `
  <article class="country">
          <img class="country__img" src="${data.flag}" />
          <div class="country__data">
            <h3 class="country__name">${data.name}</h3>
            <h4 class="country__region">${data.region}</h4>
            <p class="country__row"><span>👫</span>${(
              +data.population / 1000000
            ).toFixed(1)}</p>
            <p class="country__row"><span>🗣️</span>${data.languages[0].name}</p>
            <p class="country__row"><span>💰</span>${
              data.currencies[0].name
            }</p>
          </div>
        </article>
  `;

    countriesContainer.insertAdjacentHTML('beforeend', html);
    countriesContainer.style.opacity = 1;
  });
};

// Call back hell
const getCountryAndNeighbor = function (country) {
  // old way of handling AJAX calls
  const request = new XMLHttpRequest();

  request.open('GET', countriesAPI + 'name/' + country);
  request.send();

  request.addEventListener('load', function () {
    console.log(this);
    const [data] = JSON.parse(this.responseText);
    console.log(data);

    renderHTML(data);

    // neighbor
    const [neighbor] = data.borders;

    if (!neighbor) return;

    const request2 = new XMLHttpRequest();
    request2.open('GET', countriesAPI + '/alpha/' + neighbor);
    request2.send();

    request2.addEventListener('load', function () {
      console.log(this.responseText);

      const data2 = JSON.parse(this.responseText);
      renderHTML(data2, 'neighbour');
    });
  });
};

// getCountryData('Portugal');
// getCountryData('USA');

// getCountryAndNeighbor('Portugal');
// getCountryAndNeighbor('USA');
// getCountryAndNeighbor('Mexico');

// PROMISES
const requestPromise = fetch(countriesAPI + 'name/' + 'Portugal');
// console.log(requestPromise);

const renderError = function (msg) {
  countriesContainer.insertAdjacentText('beforeend', msg);
  countriesContainer.style.opacity = 1;
};

const fetchCountryData = function (country) {
  fetch(countriesAPI + 'name/' + country)
    .then(function (response) {
      // data is in a ReadableStream
      // console.log(response);
      return response
        .json()
        .then(function (data) {
          console.log(data); // this may throw a 404 error
          renderHTML(data[0]);

          const neighbour = data[0].borders[0];
          if (!neighbour) {
            return;
          }
          // country 2
          return fetch(countriesAPI + 'name/' + neighbour);
        })
        .then(function (response) {
          // console.log(data);
          return response.json().then(function (data) {
            console.log(data);
            renderHTML(data[0], 'neighbour');
          });
        });
    })
    .catch(function (error) {
      // catch all of the errors that will occur in the promise chain
      renderError('Something went wrong!! ' + error.message);
    })
    .finally(() => {
      // this will always be called no matter the result of the promise
      // use case, hide UI elements like ui spinners
      countriesContainer.style.opacity = 1;
    });
};

// btn.addEventListener('click', function () {
//   fetchCountryData('portugal');
// });

// I have repetitive code in the then block
const getJSON = function (url, country, errorMsg = 'Something went wrong! ') {
  return fetch(url + 'name/' + country).then((response) => {
    console.log(response);
    // create a custom error with custom message. Promise will immediately reject
    if (!response.ok) {
      throw new Error(`${errorMsg} ${response.status}`);
    }
    return response.json();
  });
};

const fetchCountryData2 = function (country) {
  fetch(countriesAPI + 'name/' + country)
    .then((response) => {
      console.log(response);
      // create a custom error with custom message. Promise will immediately reject
      if (!response.ok) {
        throw new Error(`Country not found ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      renderHTML(data[0]);
      // const neighbour = data[0].borders[0];
      const neighbour = 'xxxx';
      if (!neighbour) {
        return;
      }
      // country 2
      return fetch(countriesAPI + 'name/' + neighbour);
    })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Country not found ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      console.log(data);
      renderHTML(data[0], 'neighbour');
    })
    .catch(function (error) {
      // catch all of the errors that will occur in the promise chain
      renderError('Something went wrong!! ' + error.message);
    })
    .finally(() => {
      // this will always be called no matter the result of the promise
      // use case, hide UI elements like ui spinners
      countriesContainer.style.opacity = 1;
    });
};

const fetchCountryData3 = function (country) {
  getJSON(countriesAPI, country, 'Country not found! ')
    .then((data) => {
      renderHTML(data[0]);
      console.log(data);
      const neighbour = data[0].borders ? data[0].borders[0] : undefined;
      console.log('neg: ');
      if (!neighbour) {
        throw new Error('No neighbour found!');
      }
      // country 2
      return getJSON(countriesAPI, neighbour, 'Country not found! ');
    })
    .then((data) => {
      console.log(data);
      renderHTML(data[0], 'neighbour');
    })
    .catch(function (error) {
      // catch all of the errors that will occur in the promise chain
      renderError('Something went wrong!! ' + error.message);
    })
    .finally(() => {
      // this will always be called no matter the result of the promise
      // use case, hide UI elements like ui spinners
      countriesContainer.style.opacity = 1;
    });
};

// Challenge

const whereAmI = function (
  lat,
  long,
  errorMsg = 'Location could not be found'
) {
  // console.log(lat, long);
  return fetch(`https://geocode.xyz/${lat},${long}?geoit=json`)
    .then((response) => {
      // console.log(response.json());
      if (!response.ok) {
        throw new Error(`Something went wrong! ${errorMsg} ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      if (data.altgeocode.includes('Throttled')) {
        throw {
          msg: 'Geocode throttle exceeded\n',
          type: 'geocode',
          err: new Error('Making too many requests'),
        };
      } else {
        return data.country;
      }
    });
};

const getCountryDataWithCoords = function (lat, long) {
  whereAmI(lat, long)
    .then((data) => {
      console.log(data);
      return fetchCountryData3(data);
    })
    .catch((err) => {
      console.log(err);
      renderError('Something went wrong! ' + err.err.message);
    });
};

// // Rejected promised, will simulate by turning off network
// btn.addEventListener('click', function () {
//   // fetchCountryData3('australia');

//   getCountryDataWithCoords(52.508, 13.381);
// });

// no callback code runs first
console.log('Test Start'); // 1
setTimeout(() => {
  console.log('0 sec timer');
}, 0); // 4

Promise.resolve('Resolved promise 1').then((res) => {
  console.log(res); // 3
});
// this will block the 0 second timer from executing because it cuts the line in the micro task que
Promise.resolve('Resolved promise 2').then((res) => {
  for (let i = 0; i < 2000000000; i++) {}
  console.log(res); // 3
});
console.log('Test end'); // 2

// PROMISES: take in one parameter, the executor function. The executor function takes in two arguments, resolve, reject
// executor produces a result
const lotteryPromise = new Promise(function (resolve, reject) {
  console.log('Lottery draw is happening');
  setTimeout(() => {
    // 50/50 chance of winning
    if (Math.random() >= 0.5) {
      resolve('You WIN $$'); // promise is fulfilled: pass i data that I want to consume
    } else {
      reject(new Error('You lost $$💩'));
    }
  }, 2000);
});

// consume the promise
lotteryPromise
  .then((res) => {
    console.log(res);
  })
  .catch((err) => {
    console.log(err.message);
  });

// Promisifying setTimeout
const wait = function (seconds) {
  return new Promise(function (resolve) {
    setTimeout(resolve, seconds * 1000);
  });
};

wait(4)
  .then(() => {
    console.log('waited for 4 seconds');
    return wait(1);
  })
  .then(() => {
    console.log('waited for 1 more second');
  });

// navigator.geolocation.getCurrentPosition((position) => console.log(position)),
//   (err) => console.log(err);
// console.log('Getting position');

const getPosition = function () {
  return new Promise(function (resolve, reject) {
    // navigator.geolocation.getCurrentPosition((position) => resolve(position)),
    //   (err) => reject(err);
    navigator.geolocation.getCurrentPosition(resolve, reject);
  });
};

// getPosition().then((res) => console.log(res));

// Rejected promised, will simulate by turning off network
btn.addEventListener('click', function () {
  // fetchCountryData3('australia');

  // getCountryDataWithCoords(52.508, 13.381);
  getPosition()
    .then((res) => {
      // console.log(res.coords);
      const { latitude, longitude } = res.coords;
      // console.log(latitude, longitude);
      getCountryDataWithCoords(latitude, longitude);
      // whereAmI(latitude, longitude);
    })
    .catch((err) => {
      console.log(err.message);
    });

  // whereAmI(52.508, 13.381);
});

const images = document.querySelector('.images');
// CHALLENGE

const waiting = function (seconds) {
  return new Promise(function (resolve, reject) {
    setTimeout(() => {
      resolve(`waiting ${seconds}`);
    }, seconds * 1000);
  });
};

const createImage = function (imgPath) {
  return new Promise(function (resolve, reject) {
    const img = document.createElement('img');
    img.src = imgPath;
    // I was only missing the load event listener
    img.addEventListener('load', function () {
      images.append(img);
      resolve(img);
    });
    // look into types of event listeners
    img.addEventListener('error', function () {
      reject(new Error('Image not found'));
    });
  });
};

let currentImg;

createImage('./img/img-1.jpg')
  .then((img) => {
    currentImg = img;
    console.log('Image 1 loaded');

    return waiting(2);
  })
  .then((time) => {
    console.log(time);
    currentImg.style.display = 'none';
    return createImage('./img/img-2.jpg');
  })
  .then((img) => {
    currentImg = img;
    console.log('Image 2 loaded');
    return waiting(2);
  })
  .then(() => {
    currentImg.style.display = 'none';
  })
  .catch((err) => {
    console.log(err);
  });

// `https://geocode.xyz/${lat},${long}?geoit=json`;
const whereAmIAsync = async function () {
  try {
    // I can throw a custom error here and it will be caught in catch block
    // await stops execution until data is retrieved
    // stopping code is not blocking call stack
    const pos = await getPosition();
    const { latitude: lat, longitude: long } = pos.coords;
    const geoResponse = await fetch(
      `https://geocode.xyz/${lat},${long}?geoit=json`
    );
    const dataGeo = await geoResponse.json();
    // throw new Error('Testing error here');
    console.log(dataGeo);
    const response = await fetch(countriesAPI + 'name/' + dataGeo.country);
    const data = await response.json();
    console.log('----res-----', data[0]);
    renderHTML(data[0]);

    return `You are in ${dataGeo.city}, ${dataGeo.country}`;
  } catch (err) {
    console.log(err);
    renderError(err.message);
    throw err;
  }
};

// this returns a promise
// js does not know what the value that this function returns
// const city = whereAmIAsync();
// console.log(city);
// whereAmIAsync()
//   .then((city) => {
//     console.log(`location ${city}`);
//   })
//   .catch((err) => console.log(`2: ${err.message}`))
//   .finally(() => console.log('Done getting location'));

// converting to async
(async function () {
  try {
    const city = await whereAmIAsync();
    console.log(`location ${city}`);
  } catch (err) {
    console.log(`2: ${err.message}`);
  }
  console.log('Done getting location');
})();

try {
  let y = 1;
  const x = 2;
  x = 3;
} catch (e) {
  console.log(e);
}

const get3Countries = async function (c1, c2, c3) {
  try {
    // these are run in sequence
    // const [data1] = await getJSON(countriesAPI, c1);
    // const [data2] = await getJSON(countriesAPI, c2);
    // const [data3] = await getJSON(countriesAPI, c3);
    // console.log([data1.capital, data2.capital, data3.capital]);
    // can load then parallel

    // if one promise rejects, all will reject
    const data = await Promise.all([
      getJSON(countriesAPI, c1),
      getJSON(countriesAPI, c2),
      getJSON(countriesAPI, c3),
    ]);

    // the fastest will be the resolved promise
    // not a result all all api calls
    // this stops when a promise is fulfilled or rejected
    // await Promise.race([oneCall, twoCall...])

    console.log(data);
    console.log(data.map((d) => d[0].capital));
  } catch (err) {
    console.log(err);
  }
};

// get3Countries('portugal', 'canada', 'usa');

const timeout = function (sec) {
  return new Promise(function (_, reject) {
    setTimeout(function () {
      reject(new Error('Taking to long'));
    }, sec * 1000);
  });
};

Promise.race([getJSON(countriesAPI, 'tanzania'), timeout(0.1)])
  .then((res) => console.log(res[0]))
  .catch((err) => console.error(err));

// takes an array of apis and returns all of them settled or rejected
// unlike promise.all which will short circuit if one fails
Promise.allSettled([
  Promise.resolve('Accepted'),
  Promise.reject('Rejected'),
  Promise.resolve('Accepted'),
])
  .then((res) => console.log(res))
  .catch((err) => console.error(err));

// returns the first fulfilled promise
Promise.any([
  Promise.resolve('Accepted'),
  Promise.reject('Rejected'),
  Promise.resolve('Accepted'),
]).then((res) => console.log(res));

//// CHALLENGE

const loadNPause = async function () {
  try {
    let img = await createImage('img/img-1.jpg');
    await wait(1);
    img.style.display = 'none';
    img = await createImage('img/img-2.jpg');
    await wait(1);
    img.style.display = 'none';
    img = await createImage('img/img-3.jpg');
    await wait(1);
    img.style.display = 'none';
  } catch (err) {
    console.log(err);
  }
};

const loadAll = async function (imgArr) {
  try {
    const imgs = imgArr.map((path) => createImage(path));
    const loaded = await Promise.all(imgs);
    console.log(loaded);
    loaded.forEach(async (img) => {
      //   let me = img;
      img.classList.add('parallel');
      //   await wait(10);
      //   me.style.display = 'none';
    });

    // for (let i = 0; i < loaded.length; i++) {
    //   test = await loaded[i];
    //   await wait(2);
    //   test.style.display = 'none';
    // }
    // test = loaded[0];
    // await wait(2);
    // test.style.display = 'none';
    // test = loaded[1];
    // await wait(2);
    // test.style.display = 'none';
    // test = loaded[2];
    // await wait(2);
    // test.style.display = 'none';
  } catch (err) {
    console.log(err);
  }
};

setTimeout(() => {
  // loadNPause();
  loadAll(['img/img-1.jpg', 'img/img-2.jpg', 'img/img-3.jpg']);
}, 10000);
