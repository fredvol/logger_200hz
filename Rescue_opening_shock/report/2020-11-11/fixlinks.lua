function Link(elem)
  return pandoc.Link(elem.content, string.gsub(elem.target, "%.md$", ".html"))
end
