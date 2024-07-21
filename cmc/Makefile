# Variáveis
CXX = g++
CXXFLAGS = -std=c++11 -Wall -Iinclude
LDFLAGS =

# Arquivos fonte e objetos
SRCDIR = src
OBJDIR = obj
SOURCES = $(wildcard $(SRCDIR)/*.cpp)
OBJECTS = $(SOURCES:$(SRCDIR)/%.cpp=$(OBJDIR)/%.o)
TARGET = out

# Regras
all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CXX) $(LDFLAGS) -o $@ $^

$(OBJDIR)/%.o: $(SRCDIR)/%.cpp
	@mkdir -p $(OBJDIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJDIR) $(TARGET)

run:
	make && ./$(TARGET)

# Regra "phony" para evitar conflito com arquivos de mesmo nome
.PHONY: all clean
