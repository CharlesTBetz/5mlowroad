source "https://rubygems.org"

# Local development uses the standalone Jekyll gem. GitHub Pages deployment
# does NOT use this Gemfile — it builds via the actions/jekyll-build-pages
# GitHub Action (see .github/workflows/jekyll.yml).
gem "jekyll", "~> 4.3"

group :jekyll_plugins do
  gem "jekyll-seo-tag"
  gem "jekyll-sitemap"
end

# webrick is no longer a default gem in Ruby 3.0+, but `jekyll serve` needs it.
gem "webrick", "~> 1.8"
