import React from 'react'
import FacebookIcon from '@material-ui/icons/Facebook'
import TwitterIcon from '@material-ui/icons/Twitter'
import LinkedInIcon from '@material-ui/icons/LinkedIn'
import GitHubIcon from '@material-ui/icons/GitHub'
import GradeIcon from '@material-ui/icons/Grade'
import { WebOutlined } from '@material-ui/icons'
export default {
  name: 'Brian Mugenya',
  title: 'Full stack developer',
  birthday: '26th November 1995',
  email: 'bmugenya26@gmail.com',
  phone: '+254 700577453',
  address: 'Nairobi, Kenya',

  socials: {
    facebook: {
      link: 'https://www.facebook.com/misty.builder',
      text: 'Friend me on Facebook',
      icon: <FacebookIcon />,
    },
    twitter: {
      link: 'https://twitter.com/BrianMugenya',
      text: 'Follow me on Twitter',
      icon: <TwitterIcon />,
    },
    linkedin: {
      link: 'https://www.linkedin.com/in/brian-mugenya-007/',
      text: 'Connect with me on Linkedin',
      icon: <LinkedInIcon />,
    },
    github: {
      link: 'https://www.github.com/bmugenya',
      text: 'View my work on Github',
      icon: <GitHubIcon />,
    },
    badges: {
      link: 'https://www.youracclaim.com/users/brian-mugenya/badges',
      text: 'Find my badges on Acclaim',
      icon: <GradeIcon />,
    },
  },
  about:
    'I have a proficiency of bringing others together to resolve conflicts and reconciling differences through negotiation. I am calm and collected even under stressful situations .I am strongly passionate about innovative ideas and problem-solving using programming technologies.conscious\nI am a time conscious, self-driven Individual who is eager to learn and apply new skills and knowledge to the work place. My open minded nature allows me to work in a multi-cultural team and adapt to new cultures.',

  certifications: [
    {
      title: 'FreeCodeCamp',
      date: 'Feb 1st - (Pursuing)',
      description:
        'Front End Development Libraries\nJavaScript Algorithms and Data Structures\nResponsive Web Design',
    },
    {
      title: 'Internet Society',
      date: 'July 6th - August 19th 2018',
      description: 'Network Operations: UNIX/Linux,  Networking and DNS',
    },
    {
      title: 'Google',
      date: 'June 29th 2018',
      description: 'Google Digital Skills for Africa',
    },
  ],
  education: [
    {
      title: 'Andela',
      date: '2018 - 4 Weeks',
      description: 'Andela Cycle 35 Fellowship Bootcamp ',
    },
    {
      title: 'Africa Nazarene University',
      date: '2016 - To Date',
      description: 'Bsc. in Business Information Technology',
    },
    {
      title: 'Laiser Hill Academy ',
      date: '2013 - 2016',
      description: 'O – Level',
    },
  ],
  services: [
    {
      title: 'Web Development',
      description: 'I have been working on web design for over 4 years',
      icon: <WebOutlined />,
    },
    {
      title: 'Branding Identity',
      description: 'I will make you a brand that is catchy and leaves a trace.',
      icon: <WebOutlined />,
    },
    {
      title: 'Fast Deliver',
      description: 'I create and deliver projects as fast as possible.',
      icon: <WebOutlined />,
    },
  ],
  skills: [
    {
      title: 'FRONT-END',
      description: ['ReactJs', 'Javascript', 'Bootsrap', 'Material UI'],
    },
    {
      title: 'BACK-END',
      description: ['Flask', 'ExpressJS', 'Javascript', 'Php'],
    },
    {
      title: 'DATABASE',
      description: ['PostgreSQL', ' MySQL', 'SqlAlchemy', ' MongoDB'],
    },
  ],
  projects: [
    {
      tag: 'Flask',
      image:
        'https://res.cloudinary.com/doammcpie/image/upload/v1613579453/rafiki.png',
      title: 'Rafiki',
      caption: 'Rafiki offers a haven for anonymous communication',
      description:
        "Rafiki offers a haven for anonymous communication inorder to eradicate fear of judgment and encourage openness. Rafiki's existence was brought about due to the alarming rate of internal suffering . Rafiki consist of highly experienced counsellors and occupational health therapists as well as friends who will listen because its time you let someone know",
      links: [
        { link: 'https://rafiki-app.herokuapp.com/rafiki/' },
        {
          link: 'https://rafiki-app.herokuapp.com/rafiki/',
          icon: <GitHubIcon />,
        },
      ],
    },
    {
      tag: 'React',
      image:
        'https://res.cloudinary.com/doammcpie/image/upload/v1613579453/rafiki.png',
      title: 'Rafiki',
      caption: 'Rafiki offers a haven for anonymous communication',
      description:
        "Rafiki offers a haven for anonymous communication inorder to eradicate fear of judgment and encourage openness. Rafiki's existence was brought about due to the alarming rate of internal suffering . Rafiki consist of highly experienced counsellors and occupational health therapists as well as friends who will listen because its time you let someone know",
      links: [
        { link: 'https://rafiki-app.herokuapp.com/rafiki/' },
        {
          link: 'https://rafiki-app.herokuapp.com/rafiki/',
          icon: <GitHubIcon />,
        },
      ],
    },
    {
      tag: 'Flask',
      image:
        'https://res.cloudinary.com/doammcpie/image/upload/v1613579453/rafiki.png',
      title: 'Rafiki',
      caption: 'Rafiki offers a haven for anonymous communication',
      description:
        "Rafiki offers a haven for anonymous communication inorder to eradicate fear of judgment and encourage openness. Rafiki's existence was brought about due to the alarming rate of internal suffering . Rafiki consist of highly experienced counsellors and occupational health therapists as well as friends who will listen because its time you let someone know",
      links: [
        { link: 'https://rafiki-app.herokuapp.com/rafiki/' },
        {
          link: 'https://rafiki-app.herokuapp.com/rafiki/',
          icon: <GitHubIcon />,
        },
      ],
    },
    {
      tag: 'Flask',
      image:
        'https://res.cloudinary.com/doammcpie/image/upload/v1613579453/rafiki.png',
      title: 'Rafiki',
      caption: 'Rafiki offers a haven for anonymous communication',
      description:
        "Rafiki offers a haven for anonymous communication inorder to eradicate fear of judgment and encourage openness. Rafiki's existence was brought about due to the alarming rate of internal suffering . Rafiki consist of highly experienced counsellors and occupational health therapists as well as friends who will listen because its time you let someone know",
      links: [
        { link: 'https://rafiki-app.herokuapp.com/rafiki/' },
        {
          link: 'https://rafiki-app.herokuapp.com/rafiki/',
          icon: <GitHubIcon />,
        },
      ],
    },
  ],
}
