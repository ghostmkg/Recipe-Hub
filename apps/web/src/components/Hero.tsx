import React from 'react'

interface HeroProps {
  title?: string
  subtitle?: string
  ctaText?: string
  onCtaClick?: () => void
}

const Hero: React.FC<HeroProps> = ({
  title,
  subtitle,
  ctaText,
  onCtaClick,
}) => {
  const defaultTitle = title ?? "Welcome to Recipe Hub"
  const defaultSubtitle = subtitle ?? "Organize and visualize your Recipe Making journey."
  const defaultCtaText = ctaText ?? "Explore Now"
  const handleClick = onCtaClick ?? (() => console.log("CTA clicked!"))

  return (
    <section className="bg-gradient-to-r from-blue-600 to-indigo-700 text-white py-20 text-center rounded-2xl shadow-lg max-w-5xl mx-auto mt-10">
      <h1 className="text-4xl sm:text-5xl font-extrabold mb-4">{defaultTitle}</h1>
      <p className="text-lg sm:text-xl opacity-90 mb-8">{defaultSubtitle}</p>
      <button
        onClick={handleClick}
        className="px-6 py-3 bg-white text-blue-700 font-semibold rounded-md shadow-md hover:bg-gray-100 transition"
      >
        {defaultCtaText}
      </button>
    </section>
  )
}

export default Hero
