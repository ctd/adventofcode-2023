DAYS := $(sort $(wildcard */.))

.PHONY: all
all: $(DAYS)

.PHONY: $(DAYS)
$(DAYS):
	@echo "::group::Day $(subst /.,,$(@))"
	$(MAKE) -C "$@"
	@echo "::endgroup::"
