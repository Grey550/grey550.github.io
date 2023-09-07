South Africa Tourism and
       Activities Recommendation Website 
“Zkhiphani”
MVP Specification


Architecture


The minimum viable product includes a bare bones configuration including a front end, api and backend configuration. This configuration is meant to be able to obtain user requests, route the requests to the correct webpage(or blueprint) and records and to send back the correct information to the user.


API’s and Methods

User API - The user api will be used to allow the user to access the following functionality
Obtain data(api/activities) - Method GET:
Upload data(api/businesses) - Method PUT, POST
Delete data(api/businesses) - Method DELETE
Other API’s - The following API’s will be designed and/or added in addition to the above user api’s.
Register/ Login - an API will be designed to create user profiles and passwords, as well as business login as well.
Airbnb API - the app will use this api to be able to retrieve and post activities hosted on this site. Users will be redirected to this site when they select activities on this site.
Computicket API - the app will use this api to be able to retrieve and post activities hosted on this site. Users will be redirected to this site when they select activities on this site. 
Google maps API - this will be used to access the geolocation for the app that will allow users to find activities according to their current location.
Weather API - this will be used to display the weather conditions in the places selected by users
Date and time API - this will be used to automatically update date and time and also to use calendar options used to select events.
Data Modelling


The initial data model will be made of a relational database that will consist of only 4 tables. These tables will be classes within the model and will be the main objects that will be created. As per the stack selected this will probably be done using MySQL or PostgreSQL.


User Stories

User story 1 - a user goes to a small farm town known for its passion for school and university sports, and braais(barbecues). He arrives in the town with no one that he knows, and seems lost as he knows no one in the town. He would like to experience the best of what this little town has to offer, and although he feels there may be something interesting happening he has no idea how or where to find it. His sister suggests he try the Zkhiphani website… It ends up being a weekend of discovery and new experiences.


User Story: Reserving  a Getaway in Bloemfontein on Zkhiphani

A user intends to reserve a delightful escape in Bloemfontein, South Africa through the Zkhiphani website. The website should provide a seamless experience for the user to specify Bloemfontein as their destination. It should then display a range of lodging options, encompassing apartments, houses, and unique accommodations. Each listing should furnish comprehensive property details, encompassing photos, amenities, guest evaluations, and the host's profile. The user should have the ability to employ filters to refine their search based on factors like dates, guest count, budget, and specific amenities. Once the user discovers a lodging that captures their interest, they should be able to view the availability schedule and comprehend the complete cost of their stay. The website should ensure a secure and user-friendly reservation procedure, empowering the user to effortlessly select preferred dates, input guest details, and complete a payment. Post-reservation, the user should promptly receive an email confirming all reservation specifics. Additionally, the website should furnish a communication platform facilitating interaction with the host, alongside supplying insights into Bloemfontein's renowned attractions and cultural affairs. The website's design should adapt seamlessly to both desktop and mobile interfaces. Should the need arise to alter a reservation or revise booking details, the website should facilitate a straightforward process for such modifications. The website's content and information must remain precise, current, and localised to cater to diverse travellers visiting Bloemfontein from various global regions. Through engagement with the Zkhiphani website, the user can effortlessly uncover, secure, and savour an enchanting lodging experience in Bloemfontein, embarking on an unforgettable escapade in South Africa.
Mockups
The initial model will be based on CLI(Command Line Interface) before the full version goes live. This will allow all features to be tested before the GUI(Graphical User Interface) is built.

