# Project Proposal

For the project, we are proposing the creation of a website for Temple Cats. Temple Cats is a small TNR rescue around Temple’s main campus, with approximately 16 colony locations for feral cats. The website should be an introduction to students of the colonies. The homepage will an active slideshow of the colony cats. There could be a “kitty graveyard” type area of the website that contains all cats who have passed or been adopted. The location of noncurrent colony cats has yet to be decided. The dedicated colony pages will also have links to a wishlist/active donation links, so viewers can make donations, or alternatively, buy cat supplies straight out. However, the site needs a way to be updated weekly. Each colony page will have dedicated weekly updates, with status of the cats, as well as new images. The website is also meant to be a resource for Temple students who want to get cats, and there needs to be a way to allow large amounts of information.

# How to Run
https://www.templecats.org/

# How to Install
just a website, no need to install

# Vision

FOR warm-hearted, animal loving college students and faculty WHO desire to help their local feline community and need basic information on where their services are most necessary, The TEMPLE CATS WEBSITE is a Web-based service THAT provides critical information regarding the local cat communities including location information, veterinary contact information, and first aid guidance that improves cat prosperity at critical touch points. UNLIKE other websites dedicated to cat prosperity, OUR PRODUCT provides very detailed, geographically relevant, and practical services for free.


### Persona 1 Josh Hageman
Jason, age 18, is a first-year student studying psychology at Temple University main campus, a 
large public university in the heart of bustling North Philadelphia. He spends most of his time procrastinating from studying by watching cat videos on YouTube. He was born in a rural town northwest of Philadelphia, where his father 
runs a bakery and his mother is a school nurse. Jason’s family had a myriad of pets growing up, making Jason an avid animal lover from the time he was a young boy.


Jason’s long history with pets means has made him quite fond of being a pet owner. He greatly desires to have pets of his own; however, it is against the terms of the lease he signed with the university. He is particularly interested in using the Temple Cats website to gain more information on how he can begin caring for a cat community near his dorm.

### Persona 2 Valerie Keo
Emily is a sophomore in college. She is going for a walk in the evening, and finds a small orange kitten huddled in a pile of trash. She approaches it with food, and finds out that it is extremely friendly. She comes back with a cardboard box and carries it home. She quickly googles the basic needs of a cat and creates a makeshift litter box, and buys some cheap dry food from the nearest convenience store.

She posts on instagram about a found kitten, and someone messages her, telling her to check out the Temple Cats website to help find out what the next steps are to care for this kitten.

### Persona 3 Mikhail Sajed
Alex is 21 and a student at Temple. He adopted an adult calico cat from a shelter when he got his apartment and has been looking after it for a few months. For the past couple days the cat has not been eating regularly and Alex is worried. Alex is not familiar with any veterinarians in the area and doesn't know where to take his cat to get looked at. He heard about Temple Cats and wants to use the website in order to find out where to take his cat for a medical evaluation/ medical care.

### Persona 4 Justice Chang
Mary is the mother of a Temple Cats volunteer who just graduated. Mary would love to help out with the Temple Cats volunteer group but she does not know how to. Her kid tells her about how Temple Cats has a website where she could learn more about volunteering. Mary visits the website and instantly she is greeted by the front page. This page tells her about contact info as well as any activities that are going on in which she may be able to participate. She contacts them and the organization asks if she could drive supplies from one place to another. She agrees and checks the events section to figure out where she needs to go.

# Weekly Activites:
[a relative link to week1.md](week1.md)

[a relative link to week2.md](week2.md)

[a relative link to week3.md](week3.md)

### Fig 1. Class Diagram
![eb93fdb26af78f33ab469af9e1106111](https://user-images.githubusercontent.com/45643520/141032334-4351df26-c733-4c5a-9cba-ea9e78722919.png)

The cat class will have attributes like name, sex, alteration status, picture, etc., as well as get methods for the attributes. The colony class will have some kind of identification number, street name, number of volunteers at that location, and shelter box count, as well as get methods for the attributes. The above class diagram highlights the relationship between cat and colony. For each colony, there can be one or more cats. Each colony can have one or more cats, however, each cat can only belong to one colony. Additionally, there are the volunteer and director classes. The director class will have a name and rescue contacts, with get methods. The volunteer class will have name, colony assignments, and supply status, as well as get methods.

### Fig 2. Sequence Diagram #1: Submitting Volunteer Form
![sequence diagram one](https://github.com/CIS3296SoftwareDesignF21/prj-04-templecats/blob/valKeo-week3md/sq1.png)

The above sequence diagram demonstrates the communication between user and website application when a volunteer form is submitted. The user first navigates to the volunteer or form tab on frontend, which then communicates the form submission to the backend, which will then write the form information to the database. The backend will return a notification that the write was completed to the frontend, which will then give the user a confirmation message that form submission was successful.

### Fig 3. Sequence Diagram #2: Donation
![sequence diagram two](https://github.com/CIS3296SoftwareDesignF21/prj-04-templecats/blob/valKeo-week3md/sq2.png)

The above sequence diagram demonstrates the communication between user and website application when a user wants to donate supplies. The user will first click on the donation tab on the temple cats website. There, they will find the Amazon Wishlist link, that when clicked, will redirect the user to Amazon to complete the donation purchase.

Link to site: https://www.templecats.org/

<img width="376" alt="Screen Shot 2021-11-03 at 12 56 46 PM" src="https://user-images.githubusercontent.com/45643520/140114798-042d2b9a-099a-4c9d-9668-4dbe849b58c9.png">
<img width="371" alt="Screen Shot 2021-11-03 at 12 57 37 PM" src="https://user-images.githubusercontent.com/45643520/140116043-baf11d12-d441-4b27-96cd-cab8f48e3f73.png">


