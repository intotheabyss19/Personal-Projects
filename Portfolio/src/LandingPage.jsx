import React, { useState, useEffect } from 'react';
import { Github, Linkedin, Mail, ExternalLink, Code, Database, Brain, ArrowDown, Star, MapPin } from 'lucide-react';

const LandingPage = () => {
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const handleMouseMove = (e) => {
      setMousePosition({ x: e.clientX, y: e.clientY });
    };
    
    window.addEventListener('mousemove', handleMouseMove);
    setIsVisible(true);
    
    return () => window.removeEventListener('mousemove', handleMouseMove);
  }, []);

  const projects = [
    {
      title: "AI-Powered Analytics Dashboard",
      description: "Full-stack dashboard with ML predictions and real-time data visualization",
      tech: ["React", "Python", "TensorFlow", "PostgreSQL"],
      github: "https://github.com/yashgupta",
      live: "https://analytics-dashboard-demo.com",
      stars: 234
    },
    {
      title: "Neural Network Optimizer",
      description: "Deep learning framework optimization tool with custom algorithms",
      tech: ["Python", "PyTorch", "NumPy", "Docker"],
      github: "https://github.com/yashgupta",
      live: "https://nn-optimizer.com",
      stars: 189
    },
    {
      title: "Real-time Trading Bot",
      description: "Algorithmic trading system with predictive analytics and risk management",
      tech: ["Node.js", "React", "MongoDB", "WebSocket"],
      github: "https://github.com/yashgupta",
      live: "https://trading-bot-demo.com",
      stars: 312
    }
  ];

  const skills = [
    { icon: Code, title: "Full-Stack Development", desc: "React, Node.js, Python, PostgreSQL" },
    { icon: Database, title: "Data Analysis", desc: "Pandas, NumPy, SQL, Tableau" },
    { icon: Brain, title: "AI/ML Engineering", desc: "TensorFlow, PyTorch, Scikit-learn" }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-cyan-900 text-white overflow-hidden relative">
      {/* Animated background gradient */}
      <div 
        className="absolute inset-0 opacity-30"
        style={{
          background: `radial-gradient(circle at ${mousePosition.x}px ${mousePosition.y}px, rgba(6, 182, 212, 0.4) 0%, transparent 50%)`
        }}
      />
      
      {/* Floating particles */}
      <div className="absolute inset-0">
        {[...Array(50)].map((_, i) => (
          <div
            key={i}
            className="absolute w-2 h-2 bg-cyan-400 rounded-full opacity-20 animate-pulse"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
              animationDelay: `${Math.random() * 3}s`,
              animationDuration: `${2 + Math.random() * 3}s`
            }}
          />
        ))}
      </div>

      {/* Header */}
      <header className="relative z-10 p-6 flex justify-between items-center backdrop-blur-sm bg-black/10">
        <div className="text-2xl font-bold bg-gradient-to-r from-cyan-400 to-blue-400 bg-clip-text text-transparent">
          YG
        </div>
        <nav className="hidden md:flex space-x-8">
          <a href="#projects" className="hover:text-cyan-400 transition-colors">Projects</a>
          <a href="#skills" className="hover:text-cyan-400 transition-colors">Skills</a>
          <a href="#contact" className="hover:text-cyan-400 transition-colors">Contact</a>
        </nav>
        <div className="flex space-x-4">
          <a href="https://github.com/yashgupta" className="hover:text-cyan-400 transition-colors">
            <Github size={20} />
          </a>
          <a href="https://linkedin.com/in/yashgupta" className="hover:text-cyan-400 transition-colors">
            <Linkedin size={20} />
          </a>
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative z-10 px-6 py-20 text-center">
        <div className={`max-w-4xl mx-auto transform transition-all duration-1000 ${isVisible ? 'translate-y-0 opacity-100' : 'translate-y-10 opacity-0'}`}>
          <div className="mb-6 inline-flex items-center space-x-2 bg-cyan-500/20 backdrop-blur-sm px-4 py-2 rounded-full border border-cyan-500/30">
            <MapPin size={16} />
            <span className="text-sm">Available for opportunities</span>
          </div>
          
          <h1 className="text-6xl md:text-8xl font-bold mb-6 bg-gradient-to-r from-white via-cyan-200 to-blue-200 bg-clip-text text-transparent leading-tight">
            Yash Gupta
          </h1>
          
          <div className="text-xl md:text-2xl mb-8 text-gray-300 max-w-3xl mx-auto leading-relaxed">
            Full-Stack Developer • Data Analyst • AI/ML Engineer
            <div className="mt-4 text-lg text-gray-400">
              Crafting intelligent solutions that bridge data science and cutting-edge web technologies
            </div>
          </div>
          
          <div className="flex flex-col sm:flex-row gap-4 justify-center mb-12">
            <button className="group bg-gradient-to-r from-cyan-600 to-blue-600 px-8 py-4 rounded-full text-lg font-semibold hover:scale-105 transform transition-all duration-300 shadow-lg hover:shadow-cyan-500/25">
              <span className="flex items-center justify-center space-x-2">
                <span>View My Work</span>
                <ExternalLink size={18} className="group-hover:translate-x-1 transition-transform" />
              </span>
            </button>
            <button className="group border border-cyan-500/50 px-8 py-4 rounded-full text-lg font-semibold hover:bg-cyan-500/10 transition-all duration-300">
              <span className="flex items-center justify-center space-x-2">
                <Mail size={18} />
                <span>Get In Touch</span>
              </span>
            </button>
          </div>
          
          <div className="animate-bounce">
            <ArrowDown size={24} className="mx-auto text-cyan-400" />
          </div>
        </div>
      </section>

      {/* Skills Section */}
      <section id="skills" className="relative z-10 px-6 py-20">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-bold text-center mb-16 bg-gradient-to-r from-cyan-400 to-blue-400 bg-clip-text text-transparent">
            What I Do
          </h2>
          <div className="grid md:grid-cols-3 gap-8">
            {skills.map((skill, index) => (
              <div 
                key={index}
                className="group p-8 rounded-2xl bg-white/5 backdrop-blur-sm border border-white/10 hover:bg-white/10 transition-all duration-500 hover:scale-105"
              >
                <div className="mb-6 p-4 bg-gradient-to-br from-cyan-500/20 to-blue-500/20 rounded-xl w-fit">
                  <skill.icon size={32} className="text-cyan-400 group-hover:text-cyan-300 transition-colors" />
                </div>
                <h3 className="text-xl font-bold mb-3 text-white">{skill.title}</h3>
                <p className="text-gray-300 leading-relaxed">{skill.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Projects Section */}
      <section id="projects" className="relative z-10 px-6 py-20">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-bold text-center mb-16 bg-gradient-to-r from-cyan-400 to-blue-400 bg-clip-text text-transparent">
            Featured Projects
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {projects.map((project, index) => (
              <div 
                key={index}
                className="group p-6 rounded-2xl bg-white/5 backdrop-blur-sm border border-white/10 hover:bg-white/10 transition-all duration-500 hover:scale-105"
              >
                <div className="flex justify-between items-start mb-4">
                  <h3 className="text-xl font-bold text-white group-hover:text-cyan-300 transition-colors">
                    {project.title}
                  </h3>
                  <div className="flex items-center space-x-1 text-yellow-400">
                    <Star size={16} fill="currentColor" />
                    <span className="text-sm">{project.stars}</span>
                  </div>
                </div>
                <p className="text-gray-300 mb-4 leading-relaxed">{project.description}</p>
                <div className="flex flex-wrap gap-2 mb-6">
                  {project.tech.map((tech, i) => (
                    <span 
                      key={i}
                      className="px-3 py-1 bg-cyan-500/20 text-cyan-300 rounded-full text-sm border border-cyan-500/30"
                    >
                      {tech}
                    </span>
                  ))}
                </div>
                <div className="flex space-x-4">
                  <a 
                    href={project.github}
                    className="flex items-center space-x-2 text-gray-300 hover:text-cyan-400 transition-colors"
                  >
                    <Github size={16} />
                    <span className="text-sm">Code</span>
                  </a>
                  <a 
                    href={project.live}
                    className="flex items-center space-x-2 text-gray-300 hover:text-cyan-400 transition-colors"
                  >
                    <ExternalLink size={16} />
                    <span className="text-sm">Live Demo</span>
                  </a>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Education Section */}
      <section className="relative z-10 px-6 py-20">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-bold text-center mb-16 bg-gradient-to-r from-cyan-400 to-blue-400 bg-clip-text text-transparent">
            Education & Experience
          </h2>
          <div className="space-y-8">
            <div className="p-8 rounded-2xl bg-white/5 backdrop-blur-sm border border-white/10">
              <div className="flex flex-col md:flex-row md:justify-between md:items-start mb-4">
                <div>
                  <h3 className="text-2xl font-bold text-white mb-2">Computer Science Engineering</h3>
                  <p className="text-cyan-400 text-lg">Indian Institute of Technology</p>
                </div>
                <span className="text-gray-400 mt-2 md:mt-0">2020 - 2024</span>
              </div>
              <p className="text-gray-300 leading-relaxed">
                Specialized in Machine Learning, Data Structures & Algorithms, and Software Engineering. 
                Led multiple projects in AI/ML and full-stack development.
              </p>
            </div>
            
            <div className="p-8 rounded-2xl bg-white/5 backdrop-blur-sm border border-white/10">
              <div className="flex flex-col md:flex-row md:justify-between md:items-start mb-4">
                <div>
                  <h3 className="text-2xl font-bold text-white mb-2">Senior Full-Stack Developer</h3>
                  <p className="text-cyan-400 text-lg">TechCorp Solutions</p>
                </div>
                <span className="text-gray-400 mt-2 md:mt-0">2024 - Present</span>
              </div>
              <p className="text-gray-300 leading-relaxed">
                Leading development of AI-powered web applications, managing data pipelines, 
                and implementing machine learning models in production environments.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="relative z-10 px-6 py-20">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-4xl md:text-5xl font-bold mb-8 bg-gradient-to-r from-cyan-400 to-blue-400 bg-clip-text text-transparent">
            Let's Build Something Amazing
          </h2>
          <p className="text-xl text-gray-300 mb-12 max-w-2xl mx-auto leading-relaxed">
            I'm always excited to work on innovative projects that challenge the boundaries of technology. 
            Let's discuss how we can bring your ideas to life.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-6 justify-center items-center mb-12">
            <a 
              href="mailto:yash.gupta@email.com"
              className="group flex items-center space-x-3 bg-gradient-to-r from-cyan-600 to-blue-600 px-8 py-4 rounded-full text-lg font-semibold hover:scale-105 transform transition-all duration-300 shadow-lg hover:shadow-cyan-500/25"
            >
              <Mail size={20} />
              <span>yash.gupta@email.com</span>
            </a>
            
            <div className="flex space-x-6">
              <a 
                href="https://github.com/yashgupta"
                className="p-4 bg-white/5 backdrop-blur-sm border border-white/10 rounded-full hover:bg-white/10 transition-all duration-300 hover:scale-110"
              >
                <Github size={24} />
              </a>
              <a 
                href="https://linkedin.com/in/yashgupta"
                className="p-4 bg-white/5 backdrop-blur-sm border border-white/10 rounded-full hover:bg-white/10 transition-all duration-300 hover:scale-110"
              >
                <Linkedin size={24} />
              </a>
            </div>
          </div>
          
          <div className="text-center text-gray-400">
            <p>&copy; 2024 Yash Gupta. Crafted with React & creativity.</p>
          </div>
        </div>
      </section>
    </div>
  );
};

export default LandingPage;